"""
Given a string, 
return the number of times "am" appears in the string 
BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS.

"""

def find_between(a_string):
    a_string = str(a_string)        #convert to string
    a_string = a_string.lower()     #ignore case
    a_string = a_string.split()     #split string to list
    count = 0
    for word in a_string:           #check string for 'am'
        if word == "am":
            count += 1
    return count