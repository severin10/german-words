# https://raw.githubusercontent.com/Jonny-exe/German-Words-Library/master/German-words-1600000-words.json

import json, os, re
from pprint import pprint 

os.system("cls")    # Windows
# os.system("clear")  # Linux


with open('German-words-1600000-words.json', 'r') as file:
    words = json.load(file)

beginsWithHalb = []
endsWithBuch = []

def previewArr(arr):
    for word in arr[:20]:
        print(word)
    print('Anzahl Wörter:', len(arr), '\n')

pattern = re.compile(r'^Damm.a.{2}$')
beginsWithHalb = list(filter(pattern.search, words))

pprint(beginsWithHalb)

pattern = re.compile(r'^.{4}h.ter$')
endsWithBuch = list(filter(pattern.search, words))


def removeFirstPart(arr, str):
    outputArr = []
    for word in arr:
        newStr = re.sub(str, '', word)
        outputArr.append(newStr)
    return outputArr

secondPartBeginsWithHalb = removeFirstPart(beginsWithHalb, 'Halb')
print('Halb... ohne Halb')
previewArr(secondPartBeginsWithHalb)

def createStartsWithArray(arrStart, searchArr):
    arrSolution = []
    for startWord in arrStart:
        for endWord in searchArr:
            if(str(endWord).lower().startswith(startWord)):
                arrSolution.append(endWord)
                # print('Treffer:', endWord)   
    return arrSolution

solution = createStartsWithArray(secondPartBeginsWithHalb, endsWithBuch)

# pattern = re.compile(r'^.{1}a') # zweiter Buchstabe ist ein 'a'
# solution = list(filter(pattern.search, solution))
print('Lösung(en):')
pprint(solution)