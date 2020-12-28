largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum=int(num)
        if largest is None:
            largest = fnum
        elif largest <= fnum:
            largest = fnum
        if smallest is None:
            smallest = fnum
        elif smallest >= fnum:
            smallest = fnum
    except:
        print ("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)
