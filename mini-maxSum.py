"""Given five positive integers, find the minimum and maximum values that can be calculated 
    by summing exactly four of the five integers. Then print the respective minimum and maximum values
    as a single line of two space-separated long integers.
    Example
        arr = [1,3,5,7,9]
        The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24.
"""

def miniMaxSum(arr):
    mini_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(mini_sum, max_sum)


if __name__=="__main__":
    arr = [1,3,5,7,0]
    miniMaxSum(arr)