"""
find all numbers, 
between 2000 and 3200 (both included), 
that are divisible by 7, 
but are not a multiple of 5

The numbers obtained should be returned on a single line. 
seperated by commas.

"""

def findNums():
    nums = []         #create empty list
    for j in range(2000, 3201):      #loop through range 2000 and 3200
        if (j%7==0) and (j%5!=0):    #check numbers are divisible by 7 and not a multiple of 5
            nums.append(str(j))      #add them to the list
        
    return (','.join(nums))          #separate them with a comma

