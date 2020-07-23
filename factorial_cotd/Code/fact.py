#Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
def fact(a,b):
    stringa = str(a)  #convert value to string
    sums= a           
    stringb = stringa  
    for i in range(1,b):
        stringa = stringa + stringb  #making a+aa+aaa+aaaa (concatenating)
        sums = sums + int(stringa)   #convert to integer to add
    return sums

