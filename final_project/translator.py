import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)

# get the translator object
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    model_id = 'en-fr'
    translation = language_translator.translate(
    text=englishText,
    model_id=model_id).get_result()

    # breaking down the returned object
    the_list_of_translations = translation['translations']

    # get the first translation
    the_first_translation = the_list_of_translations[0]

    frenchText = the_first_translation['translation']

    return frenchText

def frenchToEnglish(frenchText):
    model_id = 'fr-en'
    translation = language_translator.translate(
    text=frenchText,
    model_id=model_id).get_result()

    # breaking down the returned object
    the_list_of_translations = translation['translations']

    # get the first translation
    the_first_translation = the_list_of_translations[0]

    englishText = the_first_translation['translation']
    return englishText

#print(englishToFrench("Dogs guide the blind"))
#print(frenchToEnglish("Chiens guide les aveugles"))