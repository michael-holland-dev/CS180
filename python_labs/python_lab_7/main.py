import argparse
import numpy as np
# DO NOT USE np.histogram

def main(arrayOfNumbers, numOfBins):
    # Write the code to compute the histogram here
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Histogram Generator")
    parser.add_argument("--a", nargs="+", type=int, help="Input a list of numbers to generate a histogram with")
    parser.add_argument("--b",type=int, help="Input the number of bins to use")

    parsed_args = parser.parse_args()
    main(parsed_args.a, parsed_args.b)