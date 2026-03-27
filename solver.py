from collections import Counter

with open("solutions.txt", "r") as f:
    words = f.read().splitlines()


position_counts = [Counter() for _ in range(5)]

for word in words:
    for i, letter in enumerate(word):
        position_counts[i][letter] += 1

#print(position_counts)

#for i in range(5):
    #print(i, position_counts[i].most_common(5))



for word in words:
    word_score = 0
    for i, letter in enumerate(word):
        word_score += position_counts[i][letter]
    print (word, word_score)



#print(word_scores)
#print(i, word_scores[i].most_common(5))



def score_word(word):
    score = 0
    for i, letter in enumerate(word):
        score += position_counts[i][letter]
    return score

#print(score_word("crane"))