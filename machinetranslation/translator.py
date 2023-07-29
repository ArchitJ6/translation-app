from deep_translator import MyMemoryTranslator

def english_to_french(englishText):
    #write the code here
    translator = MyMemoryTranslator(source='en-GB', target='fr-FR')
    frenchText = translator.translate(englishText)
    return frenchText

def french_to_english(frenchText):
    #write the code here
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    englishText = translator.translate(frenchText)
    return englishText


