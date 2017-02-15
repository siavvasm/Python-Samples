'''
-------------------- CSV Manipulation --------------------------

This script presents how CSV files can be manipulated using
Python.

'''
import pandas

def add_full_name(path_to_csv, path_to_new_csv):

    # Load the data into a data frame
    df = pandas.read_csv(path_to_csv)

    # Add a new column to the data frame
    df['nameFull'] = df['nameFirst'] + ' ' + df['nameLast']

    # Store the data frame contents to a new csv file
    df.to_csv(path_to_new_csv)

def main():

    # Define the paths of the desired csv files
    path_to_csv = "path/to/old.csv"
    path_to_new_csv = "path/to/new.csv"

    # Call the desired function
    add_full_name(path_to_csv, path_to_new_csv)

if __name__ == "__main__" : main()