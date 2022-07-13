"""In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
"""
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)


if __name__ == "__main__":
    arr = [1000000001,1000000002,1000000003,1000000004,1000000005]
    result = aVeryBigSum(arr)
    print(str(result))