import argparse
import numpy
import csv
# DO NOT USE scipy.spatial.cdist
# DO NOT USE THE FUNCTION np.lingalg.norm

def main(my2DList):
    # Write the code to compute the Distance Matrix
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    return None

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser("Distance Matrix Calculator")
    argument_parser.add_argument("--fpath", type=str, help="Name of the .csv file to be read in")
    parsed_args = argument_parser.parse_args()
    main(list(csv.reader(open(parsed_args.fpath))))