import argparse
import numpy as np

def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())