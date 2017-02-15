'''
--------------------- Text Mining Serial ------------------------

This script presents how the number of occurrences of the keywords
found in a desired text file can be calculated in a serial manner.

'''
import string

def main():

    # Open the desired text file and read its lines
    filename = "C:/Users/ms/Desktop/test.txt"
    fh = open(filename, 'r')
    lines = fh.readlines()

    # Initialize the dictionary that will contain the keywords frequencies
    word_counts = {}

    for line in lines:

        # Create a list containing the words of the received line
        data = line.strip().split(" ")

        for word in data:
            # Remove te punctuation of each word and make it lower case
            key = word.translate(string.punctuation).lower()

            # Check if this word exists in the dictionary
            if key in word_counts.keys():
                # If yes, increase its counter by one
                word_counts[key] += 1
            else:
                # If no, initialize its counter to one
                word_counts[key] = 1

    print(word_counts)

if __name__ == "__main__": main()
