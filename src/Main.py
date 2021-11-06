from TextProcessingClass import TextProcessing
import codecs

path = "C:\\Users\\kshir\\Desktop\\Text.txt"
file = codecs.open(path, encoding='utf-8')

Text = TextProcessing(file.read())
file.close()
print(Text.processText())

