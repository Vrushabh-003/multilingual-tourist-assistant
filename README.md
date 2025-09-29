# Multilingual Tourist Assistant 🗺️

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)

An intelligent, interactive web application built with Streamlit that serves as a personal travel planner. This assistant leverages the power of generative AI to create personalized itineraries and provides real-time information to help users plan their perfect trip.

---

## ✨ Features

- **🌐 Multilingual Support**: A fully functional interface that seamlessly switches between **English** and **Hindi**.
- **🤖 AI-Powered Itineraries**: Utilizes **Google's Gemini AI** to generate unique, personalized travel plans based on user inputs.
- **🎯 Personalization**: Recommendations are tailored to the user's destination, budget (in INR), number of travelers, and specific interests (e.g., History, Food, Adventure).
- **🌦️ Real-Time Weather**: Integrates with **WeatherAPI.com** to provide live weather forecasts for the selected travel date.
- **🆘 Emergency Hub**: A dedicated tab with essential, localized emergency contact numbers and useful phrases.
- **🔐 Secure API Management**: Follows best practices by using Streamlit's secrets management to keep API keys safe and secure.

---

## 🚀 Live Demo

## **[➡️ View Live Demo](https://tourist-assistant.streamlit.app/)** \*

## 🛠️ Tech Stack

- **Framework**: Streamlit
- **Language**: Python
- **APIs**:
  - Google Generative AI (Gemini) for recommendations
  - WeatherAPI.com for weather forecasts

---

## ⚙️ Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multilingual-tourist-assistant.git

cd multilingual-tourist-assistant

```

### 2. Create and Activate a Virtual Environment

A virtual environment is recommended to keep dependencies isolated.

### Windows:

```
python -m venv venv

.\venv\Scripts\activate
```

### macOS / Linux:

```
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 🔑 API Key Configuration

This application requires two API keys to function.

### 1. WeatherAPI.com Key

```
1. Go to WeatherAPI.com and create a free account.

2. Copy your API key from the dashboard.
```

### 2. Google AI (Gemini) Key

```
1. Go to Google AI Studio.

2. Sign in and click "Get API key" to generate your free key.
```

### Create a Secrets File

You must store these keys in a secrets.toml file.

1. Create a folder named `.streamlit` in the root of your project directory.
2. Inside `.streamlit`, create a file named `secrets.toml`.
3. Add your keys to this file in the following format:

```
# .streamlit/secrets.toml

WEATHERAPI_KEY = "your_key_from_weatherapi.com"

GOOGLE_API_KEY = "your_key_from_google_ai_studio"
```

The project's `.gitignore` file is configured to ignore this file, ensuring your keys are never committed to the repository.

### ▶️ How to Run

Once you have completed the setup and configuration, run the application with this command:

```
streamlit run app.py
```

The application will open in a new tab in your web browser.

### ☁️ Deployment

This application is designed to be deployed on Streamlit Community Cloud.

1. Push your code to a public GitHub repository (your `secrets.toml` will be ignored by Git).
2. Connect your GitHub account to Streamlit Community Cloud.
3. Select your repository and deploy.
4. Add your secrets (the contents of your local `secrets.toml` file) directly into the Streamlit deployment dashboard's secrets manager.
