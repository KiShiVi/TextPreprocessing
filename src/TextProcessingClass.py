from ReadDictClass import getDictList

conjunctionPath = ""
prepositionPath = ""
particlePath = ""
interjectionPath = ""


class TextProcessing:
    def __init__(self, text):
        if text == "" or type(text) is not str:
            raise Exception("Empty text or not string")
        self._text = text

    def processText(self):
        setOfStopWords = set(getDictList(conjunctionPath, prepositionPath, particlePath, interjectionPath))
        resultText = self._text.split(' ')
        for i in range(0, len(resultText)):
            if resultText[i] in setOfStopWords:
                resultText[i] = ''
        return ' '.join([value for value in resultText if value != ''])
