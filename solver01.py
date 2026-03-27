from collections import Counter

with open("solutions.txt", "r") as f:
    words = f.read().splitlines()
#letters = "".join(words)
#mycount = Counter(letters).most_common(6)  
#print (mycount)
#top_letters = [letter for letter, count in mycount]
#print (top_letters)

for n in words:
    score = 0
    seenletters= []    
    for m in n:
        if m in top_letters and m not in seenletters:
            score +=1
            seenletters.append(m)
        if score == 5:
            print (n, score)

position_counts = [Counter() for _ in range(5)]

for word in words:
    for i, letter in enumerate(word):
        position_counts[i][letter] += 1