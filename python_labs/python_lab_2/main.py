import json
import string
import argparse
import os

def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"


    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    