#RegEx:
import re

# Getting inputs:
file = input("Enter filename: ")
if file == "":
    file = "regex_sum_42.txt"

with open(file) as fhand:
    num_list = []
    count = 0
    for line in fhand:
        line = line.rstrip()
        extracted_strings = re.findall("[0-9]+", line)
        extracted_numbers = [int(i) for i in extracted_strings]
        sum_extracted_numbers = sum(extracted_numbers)
        count += sum_extracted_numbers
    
    print(count)