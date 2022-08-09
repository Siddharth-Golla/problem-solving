"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
"""

def sockMerchant(n, ar):
    myDict = {}
    for key in ar:
        if key in myDict:
            myDict[key] += 1
        else:
            myDict[key] = 1
    
    pair_counter = 0
    for i in myDict:
        pair_counter = pair_counter + (myDict[i] // 2)
    
    return pair_counter

if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = 9
    print(sockMerchant(n, ar))