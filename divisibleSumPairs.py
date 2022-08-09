"""
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

Example

ar = [1,2,3,4,5,6]
k = 5

Three pairs meet the criteria: [1,4],[2,3] and [4,6].
"""

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(0, n + 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                result = result + 1
    
    return result

if __name__ == '__main__':
    bar = [2, 2, 1, 3, 2, 7, 3, 2, 3, 4, 2]
    print(divisibleSumPairs(len(bar), 4, bar))

