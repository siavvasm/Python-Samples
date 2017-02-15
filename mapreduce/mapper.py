import sys
import string

def mapper():

    for line in sys.stdin:

        # Split the line into its contents
        data = line.strip().split(" ")

        # Remove punctuation and make them lower case
        for word in data:
            clean_word = word.translate(string.punctuation).lower()

        # Print the pair in the console to be used by the reducer
        print("{0}\t{1}".format(clean_word, 1))

mapper()