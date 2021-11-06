# TextPreprocessing
## Description
This program was created for text processing. 

It deletes stop words in input text
##API
```TextProcessing(text)``` - constructor receives input text

```processText() -> string``` - returns result text without stop words
## Examples
**Taking text from file in *utf-8***

```
from TextProcessingClass import TextProcessing
import codecs

path = "C:\\Users\\kshir\\Desktop\\Text.txt"
file = codecs.open(path, encoding='utf-8')

Text = TextProcessing(file.read())
file.close()
print(Text.processText())
```


**Taking text from client code**

```
from TextProcessingClass import TextProcessing
Text = TextProcessing("Hello world!")
print(Text.processText())
```

## Author
Violetta Kruglikova


