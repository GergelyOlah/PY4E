while True:
    try:
        print ("Enter")
        a = input ()
        x = float(a)
        if x==10:
            print ("This is ten")
        elif x==9:
            print ("This is nine")
        elif x<10:
            print ("This is less than ten")
        else:
            print ("This is bigger than ten")
    except:
        print ("Invalid")
