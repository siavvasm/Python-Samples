'''
---------------- Numpy, Pandas and Slicing ---------------------

This script presents how the numpy and pandas libraries are used
in order to define a custom data frame.

The correct way of extracting a slice from a desired data frame
is presented as well.

Tags: NumPy, Pandas, Slicing
'''

import numpy
import pandas

# Define the columns of the data frame
names = pandas.Series(["John Doe", "Son Walker", "Jack Smith", "Daniel Don"])
grades = pandas.Series([10, 5, 4, 2])
passed = pandas.Series([True, True, False, False])

# Construct the dictionary that describes the desired data frame
d = {"name": names, "grades": grades, "passed": passed}

# Create the data frame based on the previously constructed dictionary
df = pandas.DataFrame(d)
print(df)

# Keep only the students that passed the examination
passed = df[df["grades"] >= 5]
print(passed)

# Print the mean grade of the successful students
print("\nThe average grade of the successful students is: ")
print(numpy.mean(passed["grades"]))