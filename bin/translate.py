import requests
from bin import logger

def translate_text_deepl(text, source_lang, target_lang, api_key):
    logger.print_log("Starting translation...")
    url = "https://api.deepl.com/v2/translate"
    params = {
        "auth_key": api_key,
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang,
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        json_response = response.json()
        translated_text = json_response["translations"][0]["text"]
        logger.print_log("Translation completed!")
        return translated_text
    else:
        logger.print_log("Translation failed!")
        raise Exception(f"DeepL API request failed with status code {response.status_code}")