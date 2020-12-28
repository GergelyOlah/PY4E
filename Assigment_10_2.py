name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#Create a list with all the occurences of the hours

hrs = list()
for line in handle:
    if line.startswith("From "):
        words = line.split() #Split lines into a list of words
        time = words[5].split (":") #Split the 5th word by ":" into a list of time segments (hrs,minutes,seconds, etc)
        hrs.append(time[0]) #Add the hours (0th element of the above list) into a list

#Creaete a histogram/dictionary by counting the number of occurence of each hours
counts = dict()
for line in hrs:
    counts[line] = counts.get(line,0) + 1

#Sort the dictionary by using Tuples. item method returns a list of Tuples
for k,v in sorted(counts.items()):
    print (v,k)
