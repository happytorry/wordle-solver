from collections import Counter

with open("solutions.txt", "r") as f:
    # reads the file and splits it into a list of words
    candidates = f.read().splitlines() 