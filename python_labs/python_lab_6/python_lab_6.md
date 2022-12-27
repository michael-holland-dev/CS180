# Python Lab 6: Palindrome Number

## Description

Given an integer `x`, return `True` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

## Permitted Libraries

`import argparse`

## Deliverables
- A single .py file with your code. Be sure to print the output exactly as the test cases show.

- A single input argument to your program `--x`

## Test Cases

### Test Case 1:

Input:

`python mynetid.py --x 121`

Output:

`True`

### Test Case 2:

Input:

`python mynetid.py --x -121`

Output:

`False`

From left to right, the input reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Test Case 3:

Input:

`python mynetid.py --x 10`

Output:

`False`

The input reads 01 from right to left. Therefore, it is not a palindrome