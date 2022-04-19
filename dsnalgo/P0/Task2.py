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
telephone_number_time_spent = {}

long_time = 0
phone_number = 0


for call in calls:
    if call[0] not in telephone_number_time_spent:
        telephone_number_time_spent[call[0]] = 0
    
    if call[1] not in telephone_number_time_spent:
        telephone_number_time_spent[call[1]] = 0

    telephone_number_time_spent[call[0]] += int(call[3])

    if long_time < telephone_number_time_spent[call[0]]:
        long_time = telephone_number_time_spent[call[0]]
        phone_number = call[0]

    telephone_number_time_spent[call[1]] += int(call[3])

    if long_time < telephone_number_time_spent[call[1]]:
        long_time = telephone_number_time_spent[call[1]]
        phone_number = call[1]

print("{} spent the longest time, {} seconds, on the phone during \nSeptember 2016.".format(phone_number, long_time))