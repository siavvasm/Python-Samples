import pandas
import ggplot

def main():

    # Import the CSV file
    df = pandas.read_csv("C:/Users/ms/Desktop/data.csv")

    # Plot the data
    print
    ggplot(df, aes(xvar, yvar)) + geom_point(color='coral') + geom_line(color='coral') + \
    ggtitle('title') + xlab('x-label') + ylab('y-label')

if __name__ == "__main__": main()