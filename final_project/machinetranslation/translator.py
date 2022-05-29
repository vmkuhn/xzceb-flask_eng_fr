"""
Module for translating French to English and back via IBM Watson
"""

import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function for translating English to French via IBM Watson
    """
    if english_text is None:
        return None
    elif english_text is '':
        return ''

    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation=translation_response.get_result()

    return translation['translations'][0]['translation']


def french_to_english(french_text):
    """
    Function for translating French to English via IBM Watson
    """
    if french_text is None:
        return None
    if french_text is '':
        return ''

    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation=translation_response.get_result()

    return translation['translations'][0]['translation']
