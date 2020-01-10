import random
import os
import csv
import sys

import file_module as fm
import api_client_module as acm

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from enum import Enum

init(strip=not sys.stdout.isatty())

class RandonGenerationType(Enum):
    CSV = 1
    API = 2

def print_words_csv(words_csv):
    for i,d in enumerate(data, start=1):
        print(f"Line == {i}")
        print(f"#### {type(d)}")
        for x in d:
            print(f"        {x}")

def generate_random_word(words):
    return random.choice(words)

def mask_word(word_list):
    # Make a copy of the original list
    masked_word_list = word_list.copy()
    for index,_ in enumerate(masked_word_list):
        if index == 0 or index == len(masked_word_list)-1:
            continue
        else:
            masked_word_list[index] = str("_")
    return masked_word_list

def is_input_valid(user_input):
    # Check if input is of type str
    if not isinstance(user_input, str):
        return False

    # Check length - only single letters are allowed
    if len(user_input) > 1:
        return False    

    # Check if single character is a valid letter
    if not user_input.isalpha():
        return False

    return True

def check_letter_in_word(complete_word, word, letter):
    if letter in complete_word:
        if letter in word:
            print("Letter {} already exists. Choose another one!".format(letter))
        else:
            return [i for i, x in enumerate(complete_word) if x == letter]
    else:
        print("Letter {} does not exist".format(letter))        

def fill_word(word, indices, letter):
    for i in indices:
        word[i] = letter
    return word

cprint(figlet_format("HANGMAN", font="digital"), "red", attrs=["underline"])
randomGenType = int(input("Choose the source of random words:\t\n1. CSV\t\n2. API\n"))
    
random_word = None
if randomGenType == RandonGenerationType.CSV.value:    
    data = fm.load_csv(os.path.join(os.getcwd(),"words.csv"))
    #print_words_csv(data)

    # Store generated word
    random_word = generate_random_word(data[0])
elif randomGenType == RandonGenerationType.API.value:
    random_word = acm.get_random_from_api()

# Make it a list
random_word_list = list(char for char in random_word)

print("\nComplete this word before you run out of guesses")
# Mask it (Replace all internal chars i > 0 and i < len - 1) with _ "underscore" character
masked_word = mask_word(random_word_list)
print(masked_word)

debug = False
if debug:
    print(random_word)
    print(random_word_list, len(random_word_list))
    print(masked_word, len(masked_word))

counter = 5
win = False
while counter > 0:
    # Game Code goes here
    print("You have {} guesses left".format(counter))
    
    player_input = input("Enter a valid character: ")
    if is_input_valid(player_input):
        indices = check_letter_in_word(random_word_list, masked_word, player_input)

        if indices:
            if debug:
                print(indices, len(indices))
            print(fill_word(masked_word, indices, player_input))
        else:
            counter -= 1
    else:
        print("Invalid Input [{}] - Please enter a valid letter next time".format(player_input))
        continue

    if "_" not in masked_word:
        print("Congratulations you win. You have found the word {}".format(random_word_list))    
        break
else:
    if "_" in masked_word:
        print("You loose!")

cprint(figlet_format("COMPLETED", font="digital"), "red", attrs=["underline"])