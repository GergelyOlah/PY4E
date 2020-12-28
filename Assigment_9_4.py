name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#Creating a list out of the emails
emails = list()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        emails.append(words[1])

#Counting the emails
counts = dict()
for email in emails:
    counts[email] = counts.get(email,0)+1

#Finding the max
bigword = None
bigcount = None
for word2, count2 in counts.items():
    if bigcount is None or count2 > bigcount:
        bigword = word2
        bigcount = count2

print (bigword, bigcount)
