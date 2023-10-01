"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karin Vaculíková
email: karin.vaculikova@seznam.cz
discord: keimi_
"""
import re
from credentials import users
from task_template import TEXTS

line = ("-" * 40)

username = input("username: ")
password = input("password: ")

print(line)

if username not in users or users[username] != password:
    print("Unregistered user, terminating the program.")
    quit()

print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.", line, sep="\n")
textid = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

print(line)

if not textid.isnumeric() or int(textid) < 1 or int(textid) > len(TEXTS):
    print(f"The number must be between 1 and {(len(TEXTS))}. Terminating the program.", line, sep="\n")
    quit()

text = TEXTS[int(textid) - 1] 

words = text.strip().split()

allwords = 0
titlecase = 0
uppercase = 0
lowercase = 0
numbers = []
counts = dict()


for word in words:
    allwords += 1
    numbersInWord = [int(number) for number in re.findall(r'\d+', word)]
    if len(numbersInWord) > 0:
        numbers.extend(numbersInWord)
    elif word == word.capitalize():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1

    wordLength = len(word)
    if wordLength in counts:
        counts[wordLength] += 1
    else:
        counts[wordLength] = 1

numberSum = sum(numbers)

print(f"There are {allwords} in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {len(numbers)} numbers in the text.")
print(f"The sum of all the numbers {numberSum}")
print(line)

sortedCounts = dict(sorted(counts.items()))
maxCount = max(sortedCounts.values())

lengthColumnSize = len("LENGTH")
occurencesColumnSize = max([len("OCCURENCES"), maxCount])

def formatRow(length, count, maxCount):
    stars = "*" * count
    lengthColumn = f"{length}".rjust(lengthColumnSize)
    occurencesColumn = stars.ljust(occurencesColumnSize)
    return f"{lengthColumn} | {occurencesColumn} | {count}"

header = f"LENGTH | {'OCCURENCES'.center(occurencesColumnSize)} | COUNT"
print(header)
print("-" * len(header))

for (length, count) in sortedCounts.items():
    print(formatRow(length, count, maxCount))
    