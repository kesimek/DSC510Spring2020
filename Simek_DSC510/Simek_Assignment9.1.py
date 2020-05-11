# Katie Simek
# 10/05/2020
# Create a program that inputs a txt file, then calculate the total words, and output
# the number of occurrences of each word in the file
# seprate print function to make modification changes easier
# Have program write to a user named file with just the length of the dictionary


import string    # use to eliminate punctuation in file


def add_word(word, counts):
    counts[word] = counts.get(word, 0) + 1


def process_line(line, counts):
    line = line.rstrip()    # removes extra spaces
    line = line.lower()    # makes all words lowercase
    # makes a list of all words, removes punctuation
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()    # splits words in file
    for word in words:    # adds words to dictionary
        add_word(word, counts)


def pretty_print(counts):
    print('-' * 30)
    print('Word'.center(11) + " :  " + 'Count')
    print('-' * 30)
    # sorts by value, then for same value sorts key alpha
    for key, value in sorted(counts.items(), key=lambda kv: (kv[1], kv[0])):
        print("%s :    %d" % (key.ljust(11), value))


def process_file(counts):
    # open file to create dict
    with open(gba, 'r') as gba_file:
        for line in gba_file:
            process_line(line, counts)
    # asks user for file name, creates new file and prints length of dict
    filename = input('What would you like to call the file?')
    with open(filename, 'w') as fileHandle:
        fileHandle.write('Length of the dictionary: ' + str(len(counts)))



counts = dict()
gba = 'gettysburg.txt'
with open(gba, 'r') as gba_file:
    for line in gba_file:
        process_line(line, counts)

process_file(counts)   # gets file name, creates file and writes dict length
pretty_print(counts)   # prints dictionary and counts in program
