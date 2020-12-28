hrs = input("Enter Hours:")
h = float(hrs)
rate= input ("Rate:")
r = float(rate)
if h<=40:
    g=h*r
    print (g)
else:
    g=40*r+(h-40)*1.5*r
    print (g)
input("Press Enter to exit")
