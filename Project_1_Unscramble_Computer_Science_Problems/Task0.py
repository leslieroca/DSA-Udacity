"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    # print("READER" reader)
    # print("TEXTS" texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # print("READER" reader)
    # print("CALLS" calls)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def firstRecordText(texts):
    incoming_number = texts[0][0]
    answering_number = texts[0][1]
    time = texts[0][2]

    print("First record of texts, %s texts %s at time %s" % (incoming_number, answering_number, time))


# Testing firstRecordText
firstRecordText(texts)


def lastRecordCall(calls):
    last_call = calls[len(calls) - 1]
    incoming_number = last_call[0]
    answering_number = last_call[1]
    time = last_call[2]
    during = last_call[3]

    print("Last record of calls, %s calls %s at time %s, lasting %s seconds" % (incoming_number, answering_number, time, during))


# Testing lastRecordCall
lastRecordCall(calls)
