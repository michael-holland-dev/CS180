import argparse
import numpy as np

def main(digit_array):
    # Write the code to increment the digits by 1, and split it back into an array
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Digit Incrementer")
    parser.add_argument("--digits", nargs="+", type=int, help="Name of the file to be read in")
    args = parser.parse_args()
    main(args.digits)