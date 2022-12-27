# Python Lab 10

## Description
Feature engineering is a critical part of building a good classification or regression model. In class, we discussed engineering features from raw text emails to predict whether or not an email is spam. One set of features we looked at was word counts. 

Given a set of `n` documents, output a matrix with dimensions `n x p`, where `p` is the number of unique words over all documents.

The input to your program is a file where each row is a single document. A document ends with the newline character `\n`.  When reading the file, you will split each document (row) by the space character. This is called [tokenization](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html). For this lab, you can safely ignore punctuation (ie, no need to split `blink-182` into to two tokens `blink` and `182`).

hint: You will want to make all words lowercase so that `blink-182` and `Blink-182` are combined into a single word.

### Input:
```
blink-182 rocks\n # document 1
my favorite band is blink-182\n # document 2
blink-182 rocks green day also rocks \n # document 3
```

In this example, we have three documents and 9 **unique** words: `'also', 'band', 'blink-182', 'day', 'favorite', 'green', 'is', 'my', 'rocks'`. The output will be a matrix with dimensions `3 x 9`

The columns of your output feature matrix should correspond to words in alphanumeric order

### Output:

```
# columns: 'also', 'band', 'blink-182', 'day', 'favorite', 'green', 'is', 'my', 'rocks'
[
  [0, 0, 1, 0, 0, 0, 0, 0, 1], # document 1
  [0, 1, 1, 0, 1, 0, 1, 1, 0], # document 2
  [1, 0, 1, 1, 0, 1, 0, 0, 2], # document 3
  
]
```

## Permitted Libraries

```
import argparse
import numpy
```

## Deliverables

- Your program return the output, a 2D array with dimensions `n x p`. Be sure to return the output exactly as the test cases show.

- Your program takes a single input argument: 
  - `--fpath`, with type `str`. This is a filepath to a file containing your list of documents 
  - Each line is a new document (i.e., documents are separated by a newline character `\n`)

- A single .py file with your code

## Test Cases


### Example 1

`Input:`

`python mynetid.py --fpath input.txt`

Points to a txt file called input.txt that contains multiple documents separated by a new line:

```
blink-182 rocks
my favorite band is blink-182
blink-182 rocks green day also rocks
```

Output:

```
# Features:
[[0 0 1 0 0 0 0 0 1]
 [0 1 1 0 1 0 1 1 0]
 [1 0 1 1 0 1 0 0 2]]
```

### Example 2

Input:

`python mynetid.py --fpath input.txt`

Points to a txt file called `input.txt` that contains multiple documents separated by a new line

```
I like tacos said the cat
I also like tacos said the dog
I like tacos said the cow
The cat and the dog and the cow all like tacos
```

Output:
```
# Features:
[[0 0 0 1 0 0 1 1 1 1 1]
 [0 1 0 0 0 1 1 1 1 1 1]
 [0 0 0 0 1 0 1 1 1 1 1]
 [1 0 2 1 1 1 0 1 0 1 3]]
 ```
 
### Example 3

Input:

`python mynetid.py --fpath input.txt`

Points to a txt file called `input.txt` that contains multiple documents separated by a new line

```
Dog goes woof
Cat goes meow
Bird goes tweet
And mouse goes squeek
Cow goes moo
Frog goes croak
And the elephant goes toot
Ducks say quack
And fish go blub
```

Output:

```
# Features:
[[0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1]
 [0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0]
 [1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0]
 [0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 1 0 0]
 [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0]
 [1 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0]]
```