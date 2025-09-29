# tourist_assistant/translations.py

"""
Translation module for the Multilingual Tourist Assistant.
Contains all UI strings and a helper function to retrieve them.
"""

import streamlit as st

TRANSLATIONS = {
    "en": {
        "app_title": "Multilingual Tourist Assistant 🗺️",
        "language_select_label": "Select Language",
        "welcome_message": "Welcome! Plan Your Next Adventure.",
        
        # Tabs
        "tab_plan": "Plan Your Trip 📝",
        "tab_recommendations": "Your Recommendations ✨",
        "tab_emergency": "Emergency Info 🆘",
        "tab_weather": "Weather 🌦️",

        # Plan Your Trip Tab
        "form_header": "Tell us about your travel plans:",
        "destination_label": "Destination",
        "destination_placeholder": "e.g., Kashmir, Kerala, Mumbai",
        "date_label": "Travel Date",
        "travelers_label": "Number of Travelers",
        "budget_label": "Budget (in INR)",
        "interests_label": "Interests",
        "submit_button": "Generate Plan",
        
        # Recommendations Tab
        "recommendations_placeholder": "Submit the form in 'Plan Your Trip' to see your personalized recommendations.",
        # "recommendations_header": "Your Personalized Travel Plan for",
        "recommendations_header": "Your Personalized Travel Plan for {destination}", 
        "sub_attractions": "📍 Top Attractions",
        "sub_food": "🍽️ Food & Restaurants",
        "sub_accommodation": "🏨 Accommodation",
        "sub_transport": "🚗 Transportation",
        "mock_attraction_1": "Historic Downtown Walking Tour",
        "mock_attraction_2": "The Grand Museum of Art",
        "mock_attraction_3": "Riverside Park & Gardens",
        "mock_food_1": "The Local Spoon (Authentic Cuisine)",
        "mock_food_2": "Skyline Rooftop Bar & Grill",
        "mock_food_3": "The Corner Cafe (Breakfast & Coffee)",
        "mock_accommodation": "The Grand Heritage Hotel - A 5-star stay with excellent reviews.",
        "mock_transport": "The city's metro system is efficient and recommended. Ride-sharing apps are also widely available.",

        # Emergency Info Tab
        "emergency_header": "Essential Information",
        "emergency_numbers_header": "Key Emergency Numbers:",
        "police": "Police: 100",
        "ambulance": "Ambulance: 102",
        "fire": "Fire Department: 101",
        "disaster_management": "Disaster Management: 108",
        "useful_phrases_header": "Useful Phrases:",
        "phrase_help": "I need help. - Help.",
        "phrase_hospital": "Where is the hospital? - Hospital kahan hai?",
        "phrase_police": "Please call the police. - Police ko bulao.",
        "phrase_lost": "I am lost. - Main kho gaya/gayi hoon.",

        # Weather Tab
        "weather_placeholder": "Weather API integration is coming soon! եղ"
    },
    "hi": {
        "app_title": "बहुभाषी पर्यटक सहायक 🗺️",
        "language_select_label": "भाषा चुने",
        "welcome_message": "आपका स्वागत है! अपने अगले साहसिक कार्य की योजना बनाएं।",

        # Tabs
        "tab_plan": "अपनी यात्रा की योजना बनाएं 📝",
        "tab_recommendations": "आपकी सिफारिशें ✨",
        "tab_emergency": "आपातकालीन जानकारी 🆘",
        "tab_weather": "मौसम 🌦️",

        # Plan Your Trip Tab
        "form_header": "हमें अपनी यात्रा योजनाओं के बारे में बताएं:",
        "destination_label": "गंतव्य",
        "destination_placeholder": "उदा.,काश्मीर ,केरल , मुंबई",
        "date_label": "यात्रा की तारीख",
        "travelers_label": "यात्रियों की संख्या",
        "budget_label": "बजट (INR में)",
        "interests_label": "रुचियां",
        "submit_button": "योजना बनाएं",

        # Recommendations Tab
        "recommendations_placeholder": "अपनी व्यक्तिगत सिफारिशें देखने के लिए 'अपनी यात्रा की योजना बनाएं' में फॉर्म जमा करें।",
        # "recommendations_header": "के लिए आपकी व्यक्तिगत यात्रा योजना",
        "recommendations_header": "{destination} के लिए आपकी व्यक्तिगत यात्रा योजना",
        "sub_attractions": "📍 शीर्ष आकर्षण",
        "sub_food": "🍽️ भोजन और रेस्तरां",
        "sub_accommodation": "🏨 आवास",
        "sub_transport": "🚗 परिवहन",
        "mock_attraction_1": "ऐतिहासिक डाउनटाउन वॉकिंग टूर",
        "mock_attraction_2": "द ग्रैंड म्यूजियम ऑफ आर्ट",
        "mock_attraction_3": "रिवरसाइड पार्क और गार्डन",
        "mock_food_1": "द लोकल स्पून (प्रामाणिक व्यंजन)",
        "mock_food_2": "स्काईलाइन रूफटॉप बार और ग्रिल",
        "mock_food_3": "द कॉर्नर कैफे (नाश्ता और कॉफी)",
        "mock_accommodation": "द ग्रैंड हेरिटेज होटल - उत्कृष्ट समीक्षाओं के साथ एक 5-सितारा प्रवास।",
        "mock_transport": "शहर की मेट्रो प्रणाली कुशल है और अनुशंसित है। राइड-शेयरिंग ऐप भी व्यापक रूप से उपलब्ध हैं।",

        # Emergency Info Tab
        "emergency_header": "आवश्यक जानकारी",
        "emergency_numbers_header": "मुख्य आपातकालीन नंबर:",
        "police": "पुलिस: १००",
        "ambulance": "एम्बुलेंस: १०२",
        "fire": "दमकल विभाग: १०१",
        "disaster_management": "आपदा प्रबंधन: १०८",
        "useful_phrases_header": "उपयोगी वाक्यांश:",
        "phrase_help": "मुझे मदद चाहिए। - Madad chahiye.",
        "phrase_hospital": "अस्पताल कहाँ है? - Aspatal kahan hai?",
        "phrase_police": "कृपया पुलिस को बुलाएं। - Police ko bulao.",
        "phrase_lost": "मैं खो गया/गई हूँ। - Main kho gaya/gayi hoon.",

        # Weather Tab
        "weather_placeholder": "मौसम एपीआई एकीकरण जल्द ही आ रहा है! եղ"
    }
}

def get_translation(text_key: str) -> str:
    """
    Retrieves a translated string from the TRANSLATIONS dictionary
    based on the language stored in st.session_state.

    Args:
        text_key (str): The key for the text to be translated.

    Returns:
        str: The translated string.
    """
    lang = st.session_state.get("lang", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(text_key, f"Translation key '{text_key}' not found.")