# Python Translator

# Languages
langs = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# Imports

from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import json
import os
import shlex

for root, dirs, files in os.walk("."):
    if "config.json" in files:
        config_file_path = os.path.join(root, "config.json")
        print(f"Config file found at {config_file_path}")
        break
else:
    print("Config file not found, starting config setup")
    print("Please drag and drop your service account private key or manually enter the file path: (It is only used to authenticate with Google Translate API)")
    config_file_path = input()
    args = shlex.split(config_file_path)
    config_file_path = args[0]
    with open(config_file_path, "r") as f:
        config = json.load(f)
    with open("config.json", "w") as f:
        json.dump(config, f)

credential = service_account.Credentials.from_service_account_file(config_file_path)

translate_client = translate.Client(credentials=credential)
print("Select a language to translate to:")

for value in langs.values():
    print(value)

loop = False
chosen = False
chosen2 = False
while not loop:
    while not chosen:
        print("What language are you translating from?")
        langLongForm = input()
        langInput = list(langs.keys())[list(langs.values()).index(langLongForm)]
        if langInput.lower() not in langs:
            print("That's not a language! Please provide a correct language:")
            langLongForm = input()
            langInput = list(langs.keys())[list(langs.values()).index(langLongForm)]
        else:
            chosen2 = True
        print("Language to translate to:")
        selectedLongForm = input()
        selectedLanguage = list(langs.keys())[list(langs.values()).index(selectedLongForm)]
        if selectedLanguage.lower() not in langs:
            print("That's not a language! Please provide a correct language:")
            selectedLongForm = input()
            selectedLanguage = list(langs.keys())[list(langs.values()).index(selectedLongForm)]
        else:
            chosen = True
    print("What you want to translate:")
    translatorInput = input()
    translatorOutput = translate_client.translate(values=translatorInput, source_language=langInput, target_language=selectedLanguage, model="nmt") 
    print(f"Output language: {selectedLanguage}")
    print("Input text: {}".format(translatorOutput["input"]))
    print("Translated text: {}".format(translatorOutput["translatedText"]))
    print("Finished! do you want to do another translation? (y/n)")
    translateAgain = input()
    if translateAgain == "Y".lower():
        loop = False
    elif translateAgain == "N".lower():
        exit()
    else:
        print("die") 
        exit() 
