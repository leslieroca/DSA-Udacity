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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


#  Part A:
def prefixBangaloreCalled(calls):
    numbers = set()

    # get the areCode
    def areaCode(phone) -> str:
        prefix = ""

        for i, ch in enumerate(phone):
            if ch == ')':
                prefix = phone[0: i+1]
            elif ch == ' ' and (phone[0] == '7' or  phone[0] == '8' or phone[0] == '9'):
                prefix = phone[0: i]
            elif phone[0] == 1 and phone[1] == 4 and phone[2] == 0:
                prefix = phone[0: 3]

        return prefix



    for call in calls:
        if areaCode(call[0]) == '(080)':  # is a Bangalore number
            numbers.add(areaCode(call[1]))

    result = sorted(numbers)
    print("The numbers called by people in Bangalore have codes:\n" + "\n".join(result))



#  Part B:
    calls_from_bangalore = 0
    bangalore_to_bangalore = 0

    for call in calls:
        if areaCode(call[0]) == '(080)':
            calls_from_bangalore += 1
            if areaCode(call[1]) == '(080)':
                bangalore_to_bangalore += 1

    percent = (bangalore_to_bangalore * 100) / calls_from_bangalore

    print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % percent)





prefixBangaloreCalled(calls)