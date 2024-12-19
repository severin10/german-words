# https://raw.githubusercontent.com/Jonny-exe/German-Words-Library/master/German-words-1600000-words.json

import json, os, re
from pprint import pprint 

# os.system("cls")    # Windows
os.system("clear")  # Linux


with open('German-words-1600000-words.json', 'r') as file:
    words = json.load(file)

def addWord(wordStr):
    words.append(wordStr)
    words.sort()


addWord('Dammhaus')