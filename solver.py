from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    words = f.read().splitlines() 

# defines a function to calculate the score of a word based on the position counts
def score_word(word):
    score = 0
    seenletters= []  
    for i, letter in enumerate(word):
        if letter not in seenletters:
            score += position_counts[i][letter]
            seenletters.append(letter)
    return score

# creates a list of 5 Counter objects, one for each position in the word
position_counts = [Counter() for _ in range(5)] 

# teller antall forekomster av hver bokstav i hver posisjon
for word in words:  
    #The enumerate() function is a built-in Python tool used to iterate 
    # over a collection (like a list, tuple, or string) while keeping 
    # track of the index and the element at the same time. It returns 
    # an enumerate object that yields pairs in the form of tuples: (index, element)
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1
#print(position_counts)

word_scores = sorted ([(word, score_word(word)) for word in words], key=lambda x: x[1], reverse=True)
#print (word_scores[0:10])

first_guess = word_scores[0][0]
#f står for f-string (formatted string) — det lar deg sette inn variabler direkte i en tekst med {}.
print(f"Try this: {first_guess}")

feedback_one = list (input ("Type feedback g y x and hit enter: "))

while len (feedback_one) != 5 or any (i not in ["g", "y", "x"] for i in feedback_one):  
    #print ("Invalid feedback, try again")
    print ("Invalid feedback, try again")
    feedback_one = list(input("Type feedback g y x and hit enter: "))
    
    #feedback_one = list (feedback_one)
#print (feedback_one)

# slå av tips: settings / editor.suggest.enabled 
candidates = []


for word in words:
    keep = True
    for i in range(5):
        if feedback_one[i] == "g" and first_guess[i] != word[i]:
            keep = False

        if feedback_one[i] == "y":
            if first_guess[i] not in word or word[i] == first_guess[i]:
                keep = False

        if feedback_one[i] == "x":
            if first_guess[i] in word:
                keep = False

    if keep == True:
        candidates.append(word)
 
print (candidates)