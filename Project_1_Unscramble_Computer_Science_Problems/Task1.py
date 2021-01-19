"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


from collections import Counter

def manyDifferentNumbers(data) -> int:
    differentNumbers = set()

    for e in data:
        for i in range(2):
             differentNumbers.add(e[i])

    return len(differentNumbers)


def totalDifferentNumbers(texts, calls):
    count = manyDifferentNumbers(texts) + manyDifferentNumbers(calls)

    print("There are %s different telephone numbers in the records." % count)


# Testing totalDifferentNumbers
totalDifferentNumbers(texts, calls)