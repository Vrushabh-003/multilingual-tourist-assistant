# tourist_assistant/app.py

import streamlit as st
import pandas as pd
from datetime import date, datetime
import requests
import google.generativeai as genai

# Import from other project files
from translations import get_translation
from config import APP_CONFIG

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Tourist Assistant",
    page_icon="🗺️",
    layout="wide"
)

# --- FONT & CSS STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;700&display=swap');
    html, body, [class*="st-"], .st-emotion-cache-16txtl3 {
        font-family: 'Noto Sans Devanagari', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# # --- API KEY CONFIGURATION ---
# try:
#     OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]
#     GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
#     genai.configure(api_key=GOOGLE_API_KEY)
# except FileNotFoundError:
#     st.error("Secrets file not found. Please create a .streamlit/secrets.toml file with your API keys.")
#     st.stop()
# except KeyError:
#     st.error("API keys not found in secrets.toml. Please add OPENWEATHER_API_KEY and GOOGLE_API_KEY.")
#     st.stop()
# --- API KEY CONFIGURATION ---
try:
    # This code correctly looks for WEATHERAPI_KEY
    WEATHERAPI_KEY = st.secrets["WEATHERAPI_KEY"]
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
except FileNotFoundError:
    st.error("Secrets file not found. Please create a .streamlit/secrets.toml file with your API keys.")
    st.stop()
except KeyError as e:
    # This provides a more specific error if a key is missing
    st.error(f"The key '{e.args[0]}' was not found in your secrets.toml file. Please make sure it is spelled correctly.")
    st.stop()

# --- SESSION STATE INITIALIZATION ---
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
    st.session_state.form_data = None


# --- API & DATA FUNCTIONS (CACHED) ---

# @st.cache_data
# def get_weather_forecast(destination, travel_date):
#     """Fetches weather forecast for a destination on a specific date."""
#     base_url = "http://api.openweathermap.org/data/2.5/forecast"
#     params = {
#         "q": destination,
#         "appid": OPENWEATHER_API_KEY,
#         "units": "metric"  # Use Celsius
#     }
#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         data = response.json()
        
#         # Find the forecast for the specific travel date
#         for forecast in data['list']:
#             forecast_date = datetime.fromtimestamp(forecast['dt']).date()
#             if forecast_date == travel_date:
#                 return {
#                     "city": data['city']['name'],
#                     "temp": forecast['main']['temp'],
#                     "feels_like": forecast['main']['feels_like'],
#                     "description": forecast['weather'][0]['description'].title(),
#                     "icon": forecast['weather'][0]['icon']
#                 }
#         return {"error": "Forecast for the selected date is not available (API provides 5-day forecast)."}
#     except requests.exceptions.RequestException as e:
#         return {"error": f"API request failed: {e}"}
#     except KeyError:
#          return {"error": "Could not find the city. Please check the spelling."}

@st.cache_data
def get_weather_forecast(destination, travel_date):
    """Fetches weather forecast from WeatherAPI.com."""
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    # Format the date as YYYY-MM-DD for the API
    date_str = travel_date.strftime('%Y-%m-%d')
    
    params = {
        "key": st.secrets["WEATHERAPI_KEY"],
        "q": destination,
        "dt": date_str
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # The forecast data is in the 'forecastday' array
        forecast_data = data['forecast']['forecastday'][0]['day']
        
        return {
            "city": data['location']['name'],
            "temp": forecast_data['avgtemp_c'],
            "description": forecast_data['condition']['text'],
            "icon": forecast_data['condition']['icon']
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}
    except (KeyError, IndexError):
         return {"error": "Could not find weather data for the specified city or date. Please check the spelling or select a date within the next 14 days."}

# @st.cache_data
# def generate_personalized_plan(form_data):
#     """Generates a personalized travel plan using Google's Gemini model."""
#     # model = genai.GenerativeModel('gemini-pro')
#     model = genai.GenerativeModel('gemini-1.5-flash')
    
#     # Create a detailed prompt for the AI
#     lang_prompt = "in English" if st.session_state.lang == "en" else "in Hindi"
    
#     prompt = f"""
#     Act as an expert travel agent. Create a personalized, one-day travel plan for a trip to {form_data['destination']} for {form_data['num_travelers']} people on a budget of {form_data['budget']} USD.
#     The traveler's interests are: {', '.join(form_data['interests'])}.
#     The response should be written {lang_prompt}.
    
#     Please structure the response in Markdown with the following sections:
#     - **Summary:** A brief, exciting overview of the day.
#     - **Morning (9 AM - 1 PM):** Suggest one or two activities based on their interests. Mention estimated costs.
#     - **Lunch (1 PM - 2 PM):** Recommend a type of restaurant or specific dish that fits the budget and interests (e.g., "local street food," "a mid-range cafe").
#     - **Afternoon (2 PM - 6 PM):** Suggest one or two different activities. Mention estimated costs.
#     - **Evening (6 PM onwards):** Suggest a dinner and an evening activity.
#     - **Budget Tips:** Provide a few tips to stay within the budget.
    
#     Make the plan sound exciting and practical. Ensure the suggestions are highly relevant to the provided interests.
#     """
    
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"An error occurred while generating the plan: {str(e)}"
@st.cache_data
def generate_personalized_plan(form_data):
    """Generates a personalized travel plan using Google's Gemini model."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # --- Start of new logic ---
    # Set language for the AI's response
    lang_for_ai = "Hindi" if st.session_state.lang == "hi" else "English"
    # Set currency to INR
    currency = "INR"
    
    # Create a detailed, clean prompt for the AI
    prompt = f"""
    Act as an expert travel agent. Create a personalized, one-day travel plan for a trip to {form_data['destination']} for {form_data['num_travelers']} people on a budget of {form_data['budget']} {currency}.
    The traveler's interests are: {', '.join(form_data['interests'])}.
    The entire response must be written in {lang_for_ai}.
    
    Please structure the response in Markdown with the following sections:
    - **Summary:** A brief, exciting overview of the day.
    - **Morning (9 AM - 1 PM):** Suggest one or two activities based on their interests.
    - **Lunch (1 PM - 2 PM):** Recommend a type of restaurant or specific dish that fits the budget.
    - **Afternoon (2 PM - 6 PM):** Suggest one or two different activities.
    - **Evening (6 PM onwards):** Suggest a dinner and an evening activity.
    - **Budget Tips:** Provide a few tips to stay within the budget.
    
    Make the plan sound exciting and practical. Ensure the suggestions are highly relevant to the provided interests and the location.
    """
    # --- End of new logic ---
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the plan: {str(e)}"

# --- UI RENDERING ---

with st.sidebar:
    st.header("🗺️ Tourist Assistant")
    lang_map = {"English": "en", "हिंदी": "hi"}
    lang_selection = st.radio(
        get_translation("language_select_label"),
        options=lang_map.keys(),
        on_change=lambda: st.session_state.update(lang=lang_map[st.session_state.lang_radio]),
        key="lang_radio"
    )

st.title(get_translation("app_title"))

tab1, tab2, tab3, tab4 = st.tabs([
    get_translation("tab_plan"),
    get_translation("tab_recommendations"),
    get_translation("tab_weather"),
    get_translation("tab_emergency")
])

# --- TAB 1: PLAN YOUR TRIP ---
with tab1:
    with st.form(key="trip_planner_form"):
        st.subheader(get_translation("form_header"))
        destination = st.text_input(label=get_translation("destination_label"), placeholder=get_translation("destination_placeholder"))
        travel_date = st.date_input(label=get_translation("date_label"), min_value=date.today())
        num_travelers = st.number_input(label=get_translation("travelers_label"), min_value=1, step=1)
        budget = st.slider(label=get_translation("budget_label"), min_value=100, max_value=10000, step=50, value=1000)
        interest_options = APP_CONFIG["INTEREST_OPTIONS_HI"] if st.session_state.lang == "hi" else APP_CONFIG["INTEREST_OPTIONS"]
        interests = st.multiselect(label=get_translation("interests_label"), options=interest_options)
        
        # submitted = st.form_submit_button(get_translation("submit_button"))
        # if submitted:
        #     if not destination or not interests:
        #         st.error("Please enter a destination and select at least one interest.")
        #     else:
        #         st.session_state.form_submitted = True
        #         st.session_state.form_data = {
        #             "destination": destination, "travel_date": travel_date, "num_travelers": num_travelers,
        #             "budget": budget, "interests": interests
        #         }
        #         st.success("Plan generated! Check the other tabs for your personalized information.")
        submitted = st.form_submit_button(get_translation("submit_button"))
        if submitted:
            if not destination or not interests:
                st.error("Please enter a destination and select at least one interest.")
            else:
                # --- Start of new logic ---
                interests_for_ai = interests
                # If language is Hindi, translate interests to English for the AI model
                if st.session_state.lang == "hi":
                    interest_map = APP_CONFIG["INTEREST_MAP_HI_TO_EN"]
                    interests_for_ai = [interest_map.get(item, item) for item in interests]
                
                st.session_state.form_submitted = True
                st.session_state.form_data = {
                    "destination": destination, "travel_date": travel_date, "num_travelers": num_travelers,
                    "budget": budget, "interests": interests_for_ai # Use the translated list
                }
                # --- End of new logic ---
                st.success("Plan generated! Check the other tabs for your personalized information.")

# --- TAB 2: YOUR RECOMMENDATIONS ---
with tab2:
    if not st.session_state.form_submitted:
        st.info(get_translation("recommendations_placeholder"))
    else:
        data = st.session_state.form_data
        # st.header(f"{get_translation('recommendations_header')} **{data['destination']}**")
        st.header(get_translation('recommendations_header').format(destination=f"**{data['destination']}**"))
        with st.spinner("🤖 Crafting your personalized itinerary with AI..."):
            plan = generate_personalized_plan(data)
            st.markdown(plan)

# --- TAB 3: WEATHER ---
with tab3:
    st.header(f"🌦️ Weather Forecast")
    if not st.session_state.form_submitted:
        st.info("Submit the form in 'Plan Your Trip' to see the weather forecast.")
    else:
        data = st.session_state.form_data
        with st.spinner(f"Fetching weather for {data['destination']}..."):
            weather = get_weather_forecast(data['destination'], data['travel_date'])
            if "error" in weather:
                st.error(weather["error"])
            else:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png", width=100)
                with col2:
                    st.subheader(f"Weather in {weather['city']} on {data['travel_date'].strftime('%B %d, %Y')}")
                    # st.write(f"**Temperature:** {weather['temp']}°C (Feels like {weather['feels_like']}°C)")
                    st.write(f"**Temperature:** {weather['temp']}°C")
                    st.write(f"**Conditions:** {weather['description']}")
                

# --- TAB 4: EMERGENCY INFO ---
with tab4: # Emergency Info is now the 4th tab
    st.header(get_translation("emergency_header"))
    st.subheader(get_translation("emergency_numbers_header"))
    st.warning(f"""
    - **{get_translation("police")}**
    - **{get_translation("ambulance")}**
    - **{get_translation("fire")}**
    - **{get_translation("disaster_management")}**
    """)
    st.subheader(get_translation("useful_phrases_header"))
    st.info(f"""
    - **{get_translation("phrase_help")}**
    - **{get_translation("phrase_hospital")}**
    - **{get_translation("phrase_police")}**
    - **{get_translation("phrase_lost")}**
    """)