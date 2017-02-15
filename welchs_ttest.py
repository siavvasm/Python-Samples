import pandas
import scipy

def main():

    # Initialize constants
    filename = "";
    column_1 = "";
    column_2 = "";
    p_critical = 0.5 

    # Load the desired csv file into a dataframe
    df = pandas.read_csv(filename)

    # Perform a Welch's t test
    res = scipy.stats.ttest_ind(df[column_1], df[column_2], equal_var = False)

    # Check the null hypothesis
    if res[1] < p_critical:
        print("We should reject the null hypothesis")
        print("There is statistical significance difference between the two columns")
    else:
        print("We cannot reject the null hypothesis")
        print("There isn't statistically significant difference between the two columns")

if __name__ == "__main__" : main()