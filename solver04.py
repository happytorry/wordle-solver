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

# checks a list for words that match 
def sort_list(words, feedback, guess):
    candidates = []
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
            candidates.append(word)
    return candidates


# creates a list of 5 Counter objects, one for each position in the word
position_counts = [Counter() for _ in range(5)] 

# teller antall forekomster av hver bokstav i hver posisjon
for word in words:  
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1
#print(position_counts)

while 

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



candidates_1 = sort_list(words, feedback_one, first_guess)

print (f" There are {len(candidates_1)} words left") 
print (candidates_1)

###

# resetter
position_counts = [Counter() for _ in range(5)] 

# teller antall forekomster av hver bokstav i hver posisjon
for word in candidates_1:  
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1


word_scores = sorted ([(word, score_word(word)) for word in candidates_1], key=lambda x: x[1], reverse=True)
print (word_scores[0:10])

second_guess = word_scores[0][0]
#f står for f-string (formatted string) — det lar deg sette inn variabler direkte i en tekst med {}.
print(f"Try this as your second guess: {second_guess}")

feedback_two = list (input ("Type feedback g y x and hit enter: "))

#### 3rd guess:

candidates_2 = sort_list(candidates_1, feedback_two, second_guess)

print (f" There are {len(candidates_2)} words left") 
print (candidates_2)

###

# resetter
position_counts = [Counter() for _ in range(5)] 

# teller antall forekomster av hver bokstav i hver posisjon
for word in candidates_2:  
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1


word_scores = sorted ([(word, score_word(word)) for word in candidates_2], key=lambda x: x[1], reverse=True)
print (word_scores[0:10])

third_guess = word_scores[0][0]
#f står for f-string (formatted string) — det lar deg sette inn variabler direkte i en tekst med {}.
print(f"Try this as your third guess: {third_guess}")

feedback_three = list (input ("Type feedback g y x and hit enter: "))


#### 4th guess:

candidates_3 = sort_list(candidates_2, feedback_three, third_guess)

print (f" There are {len(candidates_3)} words left") 
print (candidates_3)

###

# resetter
position_counts = [Counter() for _ in range(5)] 

# teller antall forekomster av hver bokstav i hver posisjon
for word in candidates_3:  
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1


word_scores = sorted ([(word, score_word(word)) for word in candidates_3], key=lambda x: x[1], reverse=True)
print (word_scores[0:10])

fourth_guess = word_scores[0][0]
#f står for f-string (formatted string) — det lar deg sette inn variabler direkte i en tekst med {}.
print(f"Try this as your fourth guess: {fourth_guess}")

feedback_four = list (input ("Type feedback g y x and hit enter: "))
