import sys

def reducer():

    # Initialize values
    word_count = 0
    old_key = None

    for line in sys.stdin:

        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        # Get the key and the value
        this_key, count = data

        if old_key and old_key != this_key:
            print("{0}\t{1}".format(old_key, word_count))
            word_count = 0

        old_key = this_key
        word_count += float(count)

    if old_key and old_key != this_key:
        print("{0}\t{1}".format(old_key, word_count))

reducer()
