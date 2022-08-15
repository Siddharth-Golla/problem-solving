"""
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. 
There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm2(squared) assuming all letters are 1mm wide.

Example
 h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
 word = "torn"

The heights are t = 2,o = 1, r = 1 and n = 1. The tallest letter is 2 high and there are 4 letters.
The hightlighted area will be 2 * 4 so the answer is 8.
"""

def designerPdfViewer(h:list, word:str):
    letter_heights = []
    for letter in word:
        height = h[ord(letter) - 97]
        letter_heights.append(height)
    
    return len(word) * max(letter_heights)


if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zabaz"
    word2 = "abcd"
    print(designerPdfViewer(h, word))
    print(designerPdfViewer(h, word2))
