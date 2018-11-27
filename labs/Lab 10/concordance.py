import string

def build_concordance(filename):
    """ 
    (str) -> dict of str, list pairs
    
    Return a dictionary in which the keys are the words in the
    specified file. The value associated with each key is a list
    containing the line numbers of all the lines in which each word
    occurs.
    
    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    
    concordance = {}
    infile = open(filename, 'r')
    
    # Loop through all lines of file
    line_number = 0
    for line in infile:
        # Increment the line number so that the correct lines are 
        # added to the dictionary        
        line_number += 1 
        
        # Iterate over every word in line by splitting at
        # each space and add each word to dictionary.
        # Also removes the punctuation at the same time.
        for word in line.strip(string.punctuation).lower().split():
            # Either add the line number to a previously added word, or
            # create a new word in the dictionary.
            if word in concordance:
                if not (line_number in concordance.get(word)):
                    concordance.get(word).append(line_number)
            else:
                concordance[word] = [line_number]
    
    return concordance

def alphabetize_concordance(concordance):
    for key in sorted(concordance.keys()):
        print(str(key) + ' - ' + str(concordance[key]))
        

if __name__ == "__main__":
    concordance = build_concordance("sons_of_martha.txt")
    print(concordance)
    alphabetize_concordance(concordance)