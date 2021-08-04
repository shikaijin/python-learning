inputString = input("Please enter a sentence: ")

bigWordList = []
while (inputString != ""):
  # Process the current sentence
    wordCount = 0
    letterCount = 0
    wordList = []

    word=""
    for i in range(len(inputString)):
        letterCount = letterCount + 1
        if (inputString[i] != ' ' and inputString[i] != '.'):
            word = word + inputString[i]
        else:
            if (word != ""):
                wordList.append(word.lower())
                wordCount = wordCount + 1
                word = ""
    if (word != ""):
        wordList.append(word.lower())
        wordCount = wordCount + 1

    # Print the results for the current sentence entered
    for currentWord in wordList:
        print(currentWord)
    print("Letters: " + str(letterCount) + "   Words: " + str(wordCount))
    
    # Put the current word list to a big word list
    for currentWord in wordList:
        bigWordList.append(currentWord)
        
    inputString = input("Please enter a sentence: ")

print("---")

#count the number of times the word appears.

dictWord = {}
for currentWord in bigWordList:
    # Check if key already exists, and if so, add 1 to the value
    if currentWord in dictWord:
        dictWord[currentWord] = dictWord[currentWord] + 1
    else:
        dictWord[currentWord] = 1

# Print the results of the number of times a word appears
for dictKey, dictValue in dictWord.items():
    print(dictKey + ": " + str(dictValue))

print("---")
print("Program finished")
