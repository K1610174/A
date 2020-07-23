#Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
def fact(a,b):
    str_a = str(a) 
    sums= a
    str_b = str_a   
    for i in range(1,b):
        str_a = str_a + str_b
        sums = sums + int(str_a)
    return sums

