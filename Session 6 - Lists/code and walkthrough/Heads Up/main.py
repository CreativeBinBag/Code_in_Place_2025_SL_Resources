import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)
                
    return lines


def main():
    # your code here :) 
    # PSEUDOCODE:
    # 1. Get the list of all words from the file
    words = get_words_from_file()
    
    # 2. Start a loop that continues indefinitely (for now)
    while True:
    # 3. Inside the loop:
    #    a. Pick a random word from our list of words
         word = random.choice(words)
    #    b. Display that random word
    #    c. Wait for the user to press Enter
         input(word)

if __name__ == '__main__':
    main()