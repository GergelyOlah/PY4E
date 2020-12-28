# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
i = 0 #number of values
s = 0 #total of values
for line in fh: #The file must be read first
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        a = line.find(':')
        b = line[a+1:]
        b.lstrip()
        c = float(b)
        s = s + c
        i = i+1
    #print(line)
avg = s/i
print("Average spam confidence: "+str(avg))
