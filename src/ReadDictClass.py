def getDictList(*paths) -> list:
    listOfStopWords = []
    for path in paths:
        file = open(path, 'r')
        listOfStopWords += file.read().split('\n')
        file.close()
    return listOfStopWords
