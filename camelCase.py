"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given s, determine the number of words in s.

Example

s = oneTwoThree
There are  words in the string: 'one', 'Two', 'Three'.
Output = 3
"""

def camelcase(s):
    # Write your code here
    words = 0
    for let in s:
        if let.isupper():
            words = words + 1
    
    return words + 1


if __name__ == '__main__':
    print(camelcase("saveChangesInTheEditor"))
