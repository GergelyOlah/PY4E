#RegEx:
import re

# Getting inputs:
file = input("Enter filename: ")
if file == "":
    file = "regex_sum_1131332.txt"

with open(file) as fhand:
    count = 0
    sum_all = 0

    for line in fhand:
        line = line.rstrip()
        extracted_strings = re.findall("[0-9]+", line)
        count += len(extracted_strings)
        extracted_numbers = [int(i) for i in extracted_strings]
        sum_extracted_numbers = sum(extracted_numbers)
        sum_all += sum_extracted_numbers
    
print("There are {} numbers with a total sum: {}".format(count, sum_all))