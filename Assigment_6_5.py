#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
a = text.find(":")
b = text[a+1:]
b.lstrip() #This is an unneccessarry step since the float function automatically trips the whitespace from b.
           #And the .strip method does not change the value of b anyway without putting it into a new variable.
print (float(b))
