# Python Lab 2: Word Count

## Description
Counting words in strings is an important data science task that is used in a variety of real-world scenarios. Twitter's “Trending” feature is a large scale word count algorithm.

In this lab, you will implement a basic word counting algorithm in Python. You will want to perform the following operations on the input string:
* Separate each word in the input string (e.g., tokenization)
* Remove punctuation and special characters 
* Make each word lowercase 
* Find the count of each unique word in the string

Write the result to a .json file.

## Deliverables:
1. A single .py file with your code

2. Your program takes a single input argument: `--string` the input string

3. The program should write a .json file to the current working directory called word-counts

## Permitted Libraries
```
import json
import string
import argparse
import os
```

#### Hints:
* We’d recommend using the dictionary data structure for this assignment
* `string.punctuation` is a useful python library for handling special characters

To add a string argument to argparse:

`parser.add_argument("--string", type=str, help="string to analyze")`

To input a string from the command line, use quotes around your input string:

`python3 word-count.py --string 'blink 182 rocks'`

## Test Cases

### Test Case #1

Input:

`python mynetid.py --string "Its corn, with a big lump with knobs. It has juice. I cant imagine a more beautiful thing. Its corn, I can tell you all about it. I mean, look at this thing. When I tried it with butter everything changed."`

Output:

```
{
"its": 2,
"corn": 2,
"with": 3,
"a": 2,
"big": 1,
"lump": 1,
"knobs": 1,
"it": 3,
"has": 1,
"juice": 1,
"i": 4,
"cant": 1,
"imagine": 1,
"more": 1,
"beautiful": 1,
"thing": 2,
"can": 1,
"tell": 1,
"you": 1,
"all": 1,
"about": 1,
"mean": 1,
"look": 1,
"at": 1,
"this": 1,
"when": 1,
"tried": 1,
"butter": 1,
"everything": 1,
"changed": 1
}
```

### Test Case #2

Input:

`python mynetid.py --string "Peter Piper picked a peck of pickled peppers. Did Peter Piper pick a peck of pickled peppers. If Peter Piper picked a peck of pickled peppers, wheres the peck of pickled peppers Peter Piper picked."`

Output:

```
{
"peter": 4,
"piper": 4,
"picked": 3,
"a": 3,
"peck": 4,
"of": 4,
"pickled": 4,
"peppers": 4,
"did": 1,
"pick": 1,
"if": 1,
"wheres": 1,
"the": 1
}
```


### Test Case #3

Input: 

`python mynetid.py --string "My milkshake brings all the boys to the yard And theyre like, its better than yours, dang right its better than yours I can teach you, but I have to charge. My milkshake brings all the boys to the yard. And theyre like, its better than yours, dang right its better than yours I can teach you, but I have to charge."`


Output:

```
{
"my": 2,
"milkshake": 2,
"brings": 2,
"all": 2,
"the": 4,
"boys": 2,
"to": 4,
"yard": 2,
"and": 2,
"theyre": 2,
"like": 2,
"its": 4,
"better": 4,
"than": 4,
"yours": 4,
"dang": 2,
"right": 2,
"i": 4,
"can": 2,
"teach": 2,
"you": 2,
"but": 2,
"have": 2,
"charge": 2
}
```