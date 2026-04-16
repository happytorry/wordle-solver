from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    candidates = f.read().splitlines() 

from solver import sort_list, score_word

print(candidates[500:510])
acumulated_tries= 0
for answer in candidates[500:600]:
    local_candidates = candidates.copy()
    feedback = list ("xxxxx") 
    tries = 0
    while len(local_candidates) != 1 : #and feedback != list("ggggg"):   
        # creates a list of 5 Counter objects, one for each position in the word
        # teller antall forekomster av hver bokstav i hver posisjon
        position_counts = [Counter() for _ in range(5)] 
    
        if len(local_candidates) > 150:
            #teller hvor vanlig en bokstav er i hver posisjon 
            for word in local_candidates:  
                # "enumerate" returns an enumerate object that yields pairs in the form of tuples: (index, element)
                for i, letter in enumerate(word): # iterates through each letter in the word and its position
                    position_counts[i][letter] += 1

            #lager en liste med poeng for hvert ord, poengene måler hvor egnet ordet er som gjett 
            word_scores = sorted ([(word, score_word(word, position_counts)) for word in local_candidates], key=lambda x: x[1], reverse=True)
            #print (word_scores[0:10])
            guess = word_scores [0][0]

        #if len(candidates) < 200:
        else:
            superword_scores = []
            for word in local_candidates:
                score = 0
                #sammenligner med hvert ord i kandidatlisten og gir det feedback-kode
                for candidate in local_candidates:
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
                    score += len (sort_list(local_candidates,feedback,word))
                if word in local_candidates:
                    score -= 1
                superword_scores.append((word, score)) 
            superword_scores = sorted(superword_scores, key=lambda x: x[1] )
            #print(f"candidates: {candidates}")
            #print(f"superword_scores: {superword_scores}")

            guess = superword_scores [0][0]
        #superword_scores = sorted(superword_scores, key=lambda x: x[1])
        #print (superword_scores[0:10])
 
        # legg evnt til alle forslag som har samme score!
        #print(f"Try this: {guess}")
        tries += 1 
        if len(local_candidates) == 1:
            print(f"The solution is: {local_candidates[0]}")
            break

        print(f"Answer: {answer}, tries: {tries}", {local_candidates[0]})    
        #feedback = list (input ("Type feedback g y x and hit enter: "))
        gamefeedback = ['x'] * 5
        for i, letter in enumerate(guess):
            if guess[i] == answer[i]:
                gamefeedback[i] ="g"
            elif guess[i] in answer:
                gamefeedback[i] = "y"
            else :
                gamefeedback[i] = "x"
        #while len (feedback) != 5 or any (i not in ["g", "y", "x"] for i in feedback):  
            #print ("Invalid feedback, try again")
            #feedback = list(input("Type feedback g y x and hit enter: "))
        
        local_candidates = sort_list(local_candidates, gamefeedback, guess)
        
        
        
        #if len(candidates) == 0:
            #print ("The solution is not in my list of candidates")
            #break


        
        #print (f"There are {len(local_candidates)} words left") 
    
        #print(f"The remaining candidates are: {local_candidates}")
    #print(f"I need: {tries} tries")
    acumulated_tries += tries

print (f"The average number of tries is {acumulated_tries/100} ") 