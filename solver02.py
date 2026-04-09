from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    words = f.read().splitlines() 

# creates a list of 5 Counter objects, one for each position in the word
position_counts = [Counter() for _ in range(5)] 

for word in words:  
    #The enumerate() function is a built-in Python tool used to iterate 
    # over a collection (like a list, tuple, or string) while keeping 
    # track of the index and the element at the same time. It returns 
    # an enumerate object that yields pairs in the form of tuples: (index, element)
    for i, letter in enumerate(word): # iterates through each letter in the word and its position
        position_counts[i][letter] += 1

print(position_counts)




for word in words:
    word_score = 0
    for i, letter in enumerate(word):
        word_score += position_counts[i][letter]
    #print (word, word_score)



#print(word_scores)
#print(i, word_scores[i].most_common(5))



def score_word(word):
    score = 0
    for i, letter in enumerate(word):
        score += position_counts[i][letter]
    return score

#print(score_word("crane"))