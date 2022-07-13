"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example,
arr = [ [1,2,3],
        [4,5,6],
        [9,8,9] ]
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is 2.
"""
def diagonalDifference(arr):
    s2 = len(arr[0]) - 1
    dia1 = 0
    dia2 = 0

    for i in range(len(arr[0])):
        dia1 = dia1 + arr[i][i]
        dia2 = dia2 + arr[s2][i]
        s2 = s2 - 1

    result = abs(dia1 - dia2)
    return result


if __name__ == "__main__":
    arr = [ [56,75,86],
            [24,69,48],
            [1,90,0]]
    
    result = diagonalDifference(arr)
    print(result)