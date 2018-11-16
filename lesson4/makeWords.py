def makeWords(dictionary, hand):
    
    wordList = []
    length = len(hand)
    handCopy = hand.copy()
    print("handCopy: ",handCopy)
    count = 0
    
    for word in dictionary:
        count = 0
        print("word: ", word)
        handCopy = hand.copy()
        
        for i in range(len(word)):
            
            wordCount = word.count(word[i])           
            letterCount = hand.count(word[i])
                        
            if wordCount > letterCount:
                continue
            print("word[i]: ", word[i])
                                        
            if word[i] in handCopy:
                count += 1
                print("count: ", count)
                handCopy.pop(handCopy.index(word[i]))
                print("handCopy: ",handCopy)
                
        if count == len(word):
            wordList += [word]
            
    print("wordList: ", wordList)        
    return wordList
    
def testMakeWords():
    print("Testing makeWords()...", end="")
    
    answer = ['to']
    dictionary = ['to','cat', 'bat']
    hand = ['o','t', 't']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = ['cat']
    dictionary = ['to','cat', 'bat']
    hand = ['a','t', 'c']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = ['cat', 'bat']
    dictionary = ['to','cat', 'bat']
    hand = ['a','t', 'c', 'b']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = []
    dictionary = ['tto','cat', 'bat']
    hand = ['o','t']
    assert(makeWords(dictionary, hand) == answer)
    
    print("Passed")
    
testMakeWords()