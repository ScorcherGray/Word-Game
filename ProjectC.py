import itertools as itools
import random as rnd
from collections import defaultdict
#Larger ranges do take some time. I got the game working but not 'python fast'. I tested (3,20) which took 20 seconds.
words = []
fin = open('words.txt', 'rt')
words = fin.readlines()
fin.close()

# Create a dictionary using the length of the words as the key and a list of words as the value
words_dict = defaultdict(list)
for word in words:
    word = word.strip()
    words_dict[len(word)].append(word)
# Prompt user for the input = ("Enter the range of word lengths (low,high): "). Set low = input[0], high = input[1]
low, high = input("Enter the range of word lengths (low,high): ").split(',')
low = int(low.strip('('))
high = int(high.strip(')'))
# Pick a word at random from the list of the longest length
longWord = rnd.choice(words_dict[high])
# print(longWord)
# Use itertools combinations

choices = defaultdict(list)
#Splitting a word into a list of characters for comparison
def split(word):
    return [char for char in word]

wordLetters = split(longWord)
# This is where the slowdown happens
# Current method is to compare the number of any given letter from the 'word' in the list to the letters in the chosen word.
for num in range(low, high+1):
    choices[num] = words_dict[num].copy() # For key in lenght(low, high), create a list of 'options' include all lists from the given range
    last = len(words_dict[num])
    for word in range(0, last):
        letters = split(words_dict[num][word])
        for i in range(0, len(letters)):
            if letters.count(letters[i]) > wordLetters.count(letters[i]) and words_dict[num][word] in choices[num]:
                choices[num].remove(words_dict[num][word])  #Remove the word from choices if the conditions are met
    choices[num].sort() # Starting at low, sort the 'value' list of words alphabetically
# The old 'worst' method of permutations
# for num in range(low, high+1):
#     possible = {''.join(p) for p in itools.permutations(longWord, num)} #Permutations will give ALL words. Combinations will only give words in order
#     choices[num] = [word for word in possible if word in words_dict[num]] #Not sure how to get all words with the faster Combinations    
#     choices[num].sort() # Starting at low, sort the 'value' list of words alphabetically




guesses = defaultdict(list)
while True:
    win = True
    print(''.join(rnd.sample(longWord, k=len(longWord))),':') # Shuffle the longest word and display 'shuffled:' \n\n
    for num in range(low,high+1):
        toPrint = []
        for i in range(len(choices[num])):
            if choices[num][i] not in guesses[num]:
                toPrint.append("-" * (len(choices[num][i]))) # Will need a list of 'guesses'. If a word is not in guesses, it will be replaced by - - -
                win = False
            else:
                toPrint.append(choices[num][i])
        if toPrint != []:
            print(toPrint)
    if win:
        print("You win!")
        break
    guess = input("Enter a guess: ")
    if guess.lower() == 'q': #A way to quit the game and see the answers
        for num in range(low,high+1):
            if choices[num] != []:
                print(choices[num])
        break
    elif guess in guesses[len(guess)]:
        print("Already guessed. Try again")
    elif guess in choices[len(guess)]:
        print("Correct!")
        guesses[len(guess)].append(guess)
    else:
        print("Sorry. Try again")
        guesses[len(guess)].append(guess)
