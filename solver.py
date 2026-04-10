from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    candidates = f.read().splitlines() 

# defines a function to calculate the score of a word based on the position counts
def score_word(word):
    score = 0
    seenletters= []  
    for i, letter in enumerate(word):
        if letter not in seenletters:
            score += position_counts[i][letter]
            seenletters.append(letter)
    return score

# checks a list for words that match 
def sort_list(words, feedback, guess):
    wordcandidates = []
    for word in words:
        keep = True
        for i in range(5):
            if feedback[i] == "g" and guess[i] != word[i]:
                keep = False
            if feedback[i] == "y":
                if guess[i] not in word or word[i] == guess[i]:
                    keep = False
            if feedback[i] == "x":
                if guess[i] in word:
                    keep = False
        if keep == True:
            wordcandidates.append(word)
    return wordcandidates


#def gyldig feedback
feedback = "xxxxx"

while len(candidates) != 1 and feedback != list("ggggg"):
    # creates a list of 5 Counter objects, one for each position in the word
    position_counts = [Counter() for _ in range(5)] 
    # teller antall forekomster av hver bokstav i hver posisjon
    for word in candidates:  
        #The enumerate() function is a built-in Python tool used to iterate 
        # over a collection (like a list, tuple, or string) while keeping 
        # track of the index and the element at the same time. It returns 
        # an enumerate object that yields pairs in the form of tuples: (index, element)
        for i, letter in enumerate(word): # iterates through each letter in the word and its position
            position_counts[i][letter] += 1

    word_scores = sorted ([(word, score_word(word)) for word in candidates], key=lambda x: x[1], reverse=True)
    #print (word_scores[0:10])

    guess = word_scores[0][0]
    #f står for f-string (formatted string) — det lar deg sette inn variabler direkte i en tekst med {}.
    print(f"Try this: {guess}")

    feedback = list (input ("Type feedback g y x and hit enter: "))

    while len (feedback) != 5 or any (i not in ["g", "y", "x"] for i in feedback):  
        print ("Invalid feedback, try again")
        feedback = list(input("Type feedback g y x and hit enter: "))
    

    candidates = sort_list(candidates, feedback, guess)

    print (f" There are {len(candidates)} words left") 
    print (candidates)

###


# slå av tips: settings / editor.suggest.enabled 




