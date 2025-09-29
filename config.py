# tourist_assistant/config.py

"""
Configuration file for the Streamlit Tourist Assistant application.
"""

APP_CONFIG = {
    # Define the interest options for the multiselect widget
    "INTEREST_OPTIONS": [
        "History",
        "Food",
        "Adventure",
        "Nature",
        "Art",
        "Nightlife",
        "Shopping"
    ],

    # Define the interest options in Hindi
    "INTEREST_OPTIONS_HI": [
        "इतिहास",
        "भोजन",
        "साहसिक कार्य",
        "प्रकृति",
        "कला",
        "नाइटलाइफ़",
        "खरीदारी"
    ],
    "INTEREST_MAP_HI_TO_EN": {
        "इतिहास": "History",
        "भोजन": "Food",
        "साहसिक कार्य": "Adventure",
        "प्रकृति": "Nature",
        "कला": "Art",
        "नाइटलाइफ़": "Nightlife",
        "खरीदारी": "Shopping"
    }
}