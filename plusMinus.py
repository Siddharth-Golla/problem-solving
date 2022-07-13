""" Given an array of integers, calculate the ratios of its elements that are positive,negative, and zero.
    Print the decimal value of each fraction on a new line with places after the decimal.
#   Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,though answers with absolute error of up to  are acceptable."""


def plusMinus(arr):
    zero_count, pos_count, neg_count = 0, 0, 0
    for i, value in enumerate(arr):
        if value == 0:
            zero_count = zero_count + 1
        elif value < 0:
            neg_count = neg_count + 1
        else:
            pos_count = pos_count + 1

    print("{:.6f}".format(pos_count/len(arr)))
    print("{:.6f}".format(neg_count/len(arr)))
    print("{:.6f}".format(zero_count/len(arr)))


if __name__ == "__main__":
    arr = [0, -1, 1]
    plusMinus(arr)
