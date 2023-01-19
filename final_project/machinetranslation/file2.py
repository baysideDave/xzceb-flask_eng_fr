
"""Python interface to IBM Watson AI translator

contains code to to create a Language Translator object
includes fucntions to translate from English to French, and
from French to English:

    * englishToFrench - transslates English text to French
    * FrenchToEnglish - translates French texxt to English

"""
import sys
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator

authenticator = IAMAuthenticator(apikey)

# get the translator object

language_translator = LanguageTranslatorV3(version='2018-05-01',
        authenticator=authenticator)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    """
    Translates English text to French
    *parameter:
        englishText  UFT8 character string
        If string is empty, ***Error: No text was input*** will be returned
    """

    if len(englishText) != 0:
        try:
            model_id = 'en-fr'
            translation = \
                language_translator.translate(text=englishText,
                    model_id=model_id).get_result()
        except ApiException as ex:
            print("Method failed with status code " + str(ex.code) + ": " + ex.message)
            sys.exit('Error: Translator Failed')

        # breaking down the returned object

        the_list_of_translations = translation['translations']

        # get the first translation

        the_first_translation = the_list_of_translations[0]

        frenchText = the_first_translation['translation']
    else:
        frenchText = '***Error: No text was input***'

    return frenchText


def frenchToEnglish(frenchText):
    """
    Translates  French text to English
    *parameter:
        frenchText  UFT8 character string
        If string is empty, ***Error: No text was input*** will be returned
    """

    if len(frenchText) != 0:
        try:
            model_id = 'fr-en'
            translation = \
                language_translator.translate(text=frenchText,
                    model_id=model_id).get_result()
        except ApiException as ex:
            print("Method failed with status code " + str(ex.code) + ": " + ex.message)
            sys.exit('Error: Translator Failed')

        # breaking down the returned object

        the_list_of_translations = translation['translations']

        # get the first translation

        the_first_translation = the_list_of_translations[0]

        englishText = the_first_translation['translation']
    else:
        englishText = '***Error: No text was input***'
    return englishText