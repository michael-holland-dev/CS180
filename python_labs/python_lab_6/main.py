import argparse

def main(number: int):
    # Write the code to determine whether or not a number is a pallindrome here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    
    return None

if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)