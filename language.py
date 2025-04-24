# localization.py

translations = {
    "ru": {
        "weight_prompt": "Укажите вес и рост",
        "description": "Это нужно чтобы составить индивидуальный план",
        "next": "Дальше",
        "unit_kg": "кг",
        "unit_lb": "фунты"
    },
    "en": {
        "weight_prompt": "Enter your weight and height",
        "description": "This is needed to create a personalized plan",
        "next": "Next",
        "unit_kg": "kg",
        "unit_lb": "lbs"
    }
}

current_lang = "ru"


def set_language(lang_code):
    global current_lang
    current_lang = lang_code

def tr(key):
    return translations.get(current_lang, {}).get(key, key)

