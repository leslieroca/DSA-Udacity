"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def numberWithLongestTimeOnThePhone(calls):
    numbers = {}

    for call in calls:
        for i in range(2):
            if not call[i] in numbers:
                numbers[call[i]] = int(call[3])
            else: numbers[call[i]] += int(call[3])

    telephone_number = max(numbers.keys(), key=(lambda x: numbers[x]))
    total_time = numbers[telephone_number]

    print("%s spent the longest time, %s seconds, on the phone during September 2016." % (telephone_number, total_time))



numberWithLongestTimeOnThePhone(calls)
