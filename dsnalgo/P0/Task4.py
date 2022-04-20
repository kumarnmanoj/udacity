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

tm_prefix_send_message = set()
tm_prefix_receive_message = set()
tm_prefix_made_calls = set()
tm_prefix_received_calls = set()

for text in texts:
    tm_prefix_send_message.add(text[0])
    tm_prefix_receive_message.add(text[1])

for call in calls:
    tm_prefix_made_calls.add(call[0])
    tm_prefix_received_calls.add(call[1])

def is_telemarketing_caller(caller):
    not_in_creceived = caller not in tm_prefix_received_calls
    not_in_mreceived = caller not in tm_prefix_receive_message
    not_in_message_sent = caller not in tm_prefix_send_message

    return not_in_creceived and not_in_mreceived and not_in_message_sent

possible_tele_marketers = list(filter(is_telemarketing_caller, tm_prefix_made_calls))

print("These numbers could be telemarketers: ")

for possible_tele_marketer in sorted(possible_tele_marketers):
    print(possible_tele_marketer)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:

<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

