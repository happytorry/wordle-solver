from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    candidates = f.read().splitlines() 

with open("words.txt", "r") as f:
    # reads the file and splits it into a list of words
    words = f.read().splitlines() 

words = candidates

# defines a function to calculate the score of a word based on the position counts
# Scores a word based how common each letter in each position is compared to the all the words in list (candidates) Use positioncounts
def score_word(word, position_counts):
    score = 0
    seenletters= []  
    for i, letter in enumerate(word):
        if letter not in seenletters:
            score += position_counts[i][letter]
            seenletters.append(letter)
    return score



# sorts a list: "words" for words that match based on a guess and the feedback the guess it gets. Keeps the remaining candidates
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
        if keep:
            wordcandidates.append(word)
    return wordcandidates

if __name__ == "__main__":
    #def gyldig feedback
    feedback = list ("xxxxx") 

    while len(candidates) != 1 and feedback != list("ggggg"):   
        # creates a list of 5 Counter objects, one for each position in the word
        # teller antall forekomster av hver bokstav i hver posisjon
        position_counts = [Counter() for _ in range(5)] 
    
        if len(candidates) > 150:
            #teller hvor vanlig en bokstav er i hver posisjon 
            for word in candidates:  
                # "enumerate" returns an enumerate object that yields pairs in the form of tuples: (index, element)
                for i, letter in enumerate(word): # iterates through each letter in the word and its position
                    position_counts[i][letter] += 1

            #lager en liste med poeng for hvert ord, poengene måler hvor egnet ordet er som gjett 
            word_scores = sorted ([(word, score_word(word, position_counts)) for word in candidates], key=lambda x: x[1], reverse=True)
            #print (word_scores[0:10])
            guess = word_scores [0][0]

        #if len(candidates) < 200:
        else:
            superword_scores = []
            for word in words:
                score = 0
                #sammenligner med hvert ord i kandidatlisten og gir det feedback-kode
                for candidate in candidates:
                    feedback = ['x'] * 5
                    for i, letter in enumerate(word):
                        if word[i] == candidate[i]:
                            feedback[i] ="g"
                        elif word[i] in candidate:
                            feedback[i] = "y"
                        else :
                            feedback[i] = "x"
                    # gir ordet en score for denne komboen og legger til score for tidligere komboer
                    # checks a list for words that match, score er antall ord i igjen i candidates 
                    score += len (sort_list(candidates,feedback,word))
                if word in candidates:
                    score -= 1
                superword_scores.append((word, score)) 
            superword_scores = sorted(superword_scores, key=lambda x: x[1] )
            guess = superword_scores [0][0]


        #superword_scores = sorted(superword_scores, key=lambda x: x[1])
        #print (superword_scores[0:10])
        
        # legg evnt til alle forslag som har samme score!
        print(f"Try this: {guess}")

        feedback = list (input ("Type feedback g y x and hit enter: "))

        while len (feedback) != 5 or any (i not in ["g", "y", "x"] for i in feedback):  
            print ("Invalid feedback, try again")
            feedback = list(input("Type feedback g y x and hit enter: "))
        
        candidates = sort_list(candidates, feedback, guess)

        if len(candidates) == 0:
            print ("The solution is not in my list of candidates")
            break

        if len(candidates) == 1:
            print(f"The solution is: {candidates[0]}")
            break

        print (f"There are {len(candidates)} words left") 
    
        print(f"The remaining candidates are: {candidates}")
    

###


# slå av tips: settings / editor.suggest.enabled 




