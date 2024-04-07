import random
from collections import defaultdict

with open("5 letter word dictionary.txt", 'r') as dictionary:
    dictionary = dictionary.read().split('\n')

word = random.choice(dictionary)

word_placement = defaultdict(set)

for i in range(len(word)):
    word_placement[word[i]].add(i)


places = ['-'] * len(word)
seen_letters = set()
seen_words = set()


tries = 0

GUESS_LENGTH = 5 

while True:
    if tries == 5: 
        print(f"You did not guess the word!\nThe word was {word}")
        break
    user_inp = input(">>").lower()

    if user_inp == "quit":
        break

    if len(user_inp) != GUESS_LENGTH: 
        print("Your input must be 5 letters long")
        continue

    if not user_inp in dictionary:
        print("Your word is not in the dictionary")
        continue

    if user_inp == word:
        print(f"You guessed the word in {tries} tries")
        break

    if user_inp in seen_words:
        print(f"The word {user_inp}, has already been guessed")
        continue
    
    seen_words.add(user_inp)

    for char in user_inp:
        if char in seen_letters:
            continue 
        seen_letters.add(char)
        if char in word_placement:
            for c in word_placement[char]:
                places[c] = char

    if ''.join(places) == word:
        print('You won!')
        break
    state = ''.join(places)

    print(state)

    tries += 1
    