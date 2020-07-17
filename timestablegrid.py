#challenge of the day friday week 2
# Given integer n, write a python function which returns a times table grid for all the integers between 1 and n. The grid should be separated by tabs and new lines.

n = int(input("Enter a number here: "))

def timesTable(n): 
    string = ""  
    for i in range(1,n+1):
        for j in range(1,n+1):
            string += str(i*j) + "\t"
        string += "\n"
    return (string)
      
print( timesTable(n))


# another formating option ----print (("{:3}".format(i*j)), end=' ')-----