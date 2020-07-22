    #words as a string input
    #sorts each item alphanumerically
    #removes duplicates 
    #return the result

def dupes(input):
    words = [word for word in input.split(" ")]
    return (" ".join(sorted(list(set(words)))))


