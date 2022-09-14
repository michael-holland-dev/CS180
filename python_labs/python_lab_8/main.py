import argparse
import math
import csv

def main(my2DList):
    # Write the code to compute the Covariance Matrices
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    return None

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser("Covariance Matrix Calculator")
    argument_parser.add_argument("--fpath", type=str, help="Name of the .csv file to be read in")
    parsed_args = argument_parser.parse_args()
    main(list(csv.reader(open(parsed_args.fpath))))