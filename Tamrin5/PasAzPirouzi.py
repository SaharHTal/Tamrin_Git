import re
n = int(input())
sentence = input()
sentence = re.sub(r"[^a-zA-Z\u0600-\u06FF\s]", "", sentence)
sentence = re.sub("،", "", sentence)
target_word = input()
words = sentence.split()
for word in words:
    distance = 0
    if len(word) == len(target_word):
        for letter1, letter2 in zip(target_word, word):
            if letter1 != letter2:
                distance += 1
    elif len(word) < len(target_word):
        word2 = word + ("_" * (len(target_word) - len(word)))
        for letter1, letter2 in zip(target_word, word2):
            if letter1 != letter2:
                distance += 1
    elif len(word) > len(target_word):
        for letter1, letter2 in zip(target_word, word):
            if letter1 != letter2:
                distance += 1
        distance += (len(word) - len(target_word))
    if distance <= n:
        print(word)


