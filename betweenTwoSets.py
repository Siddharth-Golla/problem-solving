"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1) The elements of the first array are all factors of the integer being considered
2) The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
a = [2,6]
b = [24,36]
There are two numbers between the arrays: 6 and 12.
6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the first value.
12 % 2 = 0, 12 % 6 = 0, 24 % 12 = 0 and 36 % 12 = 0 for the second value.
Therefore return 2
"""

def getTotalX(a, b):
    result_list = []
    max_desired = min(b)
    i = 1
    while i < max_desired + 1:
        first_cond = True
        second_cond = True
        for num in a:
            if i % num != 0:
                first_cond = False
                break
        
        if first_cond:
            for num in b:
                if num % i != 0:
                    second_cond = False
                    break
        
        if first_cond and second_cond:
            result_list.append(i)
        
        i = i + 1

    
    return result_list

if __name__ == '__main__':
    a = [2, 4]
    b = [16, 32, 96]

    print(getTotalX(a,b))