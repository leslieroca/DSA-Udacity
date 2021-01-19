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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketersNumbers(texts, calls):

    # Set of numbers that send and receive texts
    text_set = set()
    for text in texts:
        text_set.update(text[:2])



    # Set of numbers that receive incoming callas
    receive_calls_set = set()
    for call in calls:
        receive_calls_set.add(call[1])


    # Checking for telemarketers numbers that are not in receive_calls_set not in text_set
    telemarketer_number_set = set()
    for call in calls:
        if call[0] not in text_set and call[0] not in receive_calls_set:
            telemarketer_number_set.add(call[0])



    telemarketer_number_list = sorted(telemarketer_number_set)
    print("These numbers could be telemarketers:\n" + "\n".join(telemarketer_number_list))




telemarketersNumbers(texts, calls)