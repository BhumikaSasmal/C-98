def countWordsFromFile():
    fileName = input("Enter file Name.")
    file = open(fileName, "r")
    wordCount = 0
    for line in file :
        words = line.split()
        wordCount += len(words)
    print("number of words is" + str(wordCount))

countWordsFromFile()

