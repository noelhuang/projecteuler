def palindromecheck(word):
    # Do some cleaning first
    word = word.lower()
    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    wordlist= []
    for i in range(0, len(word)):
        if word[i] in letterlist:
            wordlist.append(word[i])

    word = ""

    # Convert wordlist back into a string, a.k.a. word

    for i in range(0, len(wordlist)):
        word = word + wordlist[i]

    # Actual checkl if the word is a palindrome

    if len(word) % 2 == 0:
        print("The word/sentence has an even number of letters")
        halfsize = len(word) // 2
        firsthalf = []
        secondhalf = []

        # half listmaker

        for i in range(0, halfsize):
            firsthalf.append(word[i])
        for i in range(halfsize, len(word)):
            secondhalf.append(word[i])

        palindromeflag = True

        for i in range(0, len(firsthalf)):
            if firsthalf[i] == secondhalf[-(i + 1)]:
                palindromeflag = True
            if firsthalf[i] != secondhalf[-(i + 1)]:
                palindromeflag = False
            if palindromeflag is False:
                print("This word is not a palindrome")
                break

    else:
        print("This word/sentence has an uneven number of letters")
        halfsize = len(word) // 2
        firsthalf = []
        secondhalf = []

        # half listmaker

        for i in range(0, halfsize):
            firsthalf.append(word[i])
        for i in range(halfsize + 1, len(word)):
            secondhalf.append(word[i])

        palindromeflag = True

        for i in range(0, len(firsthalf)):
            if firsthalf[i] == secondhalf[-(i + 1)]:
                palindromeflag = True
            if firsthalf[i] != secondhalf[-(i + 1)]:
                palindromeflag = False
            if palindromeflag is False:
                print("This word is not a palindrome")
                break

    if palindromeflag is True:
        print("This word/sentence is a palindrome")


palindromecheck("A man, a plan, a canal: Panama")
