# Multilingual Tourist Assistant

## Description

A user-friendly, interactive web application built with Streamlit to help tourists plan their trips. The application is fully multilingual, supporting both English and Hindi. It allows users to input their travel preferences and receive mock recommendations for attractions, food, and more.

## ✨ Features

- **🌐 Multilingual Support**: Instantly switch between English and Hindi interfaces.
- **📝 Trip Planning Form**: A comprehensive form to capture travel details like destination, dates, budget, and interests.
- **💡 Personalized Recommendations**: Generates a mock travel plan based on user input (cached for efficiency).
- **🆘 Emergency Information**: Provides a quick-access tab with essential emergency contacts and useful phrases in the selected language.
- ** modular and Clean Code**: The project is structured into separate files for logic, configuration, and translations for better maintainability.
- **State Management**: Uses Streamlit's `st.session_state` to persist user language preference and form data across reruns and tabs.

## 🛠️ Setup and Installation

Follow these steps to set up the project on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd tourist_assistant
    ```

2.  **Create and activate a virtual environment:**
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 How to Run

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py