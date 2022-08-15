"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
Each summer, its height increases by 1 meter. A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring.
How tall will the tree be after n growth cycles?

For example, if the number of growth cycles is n=5, the calculations are as follows:
Period      Height
0           1
1           2
2           3
3           6
4           7
5           14
"""

def utopianTree(n:int):
    height = 2
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        for i in range(2,n + 1):
            if i%2 == 0:
                height = height + 1
            else:
                height = height * 2
        return height
    


if __name__ == '__main__':
    for i in range(61):
        print(i, utopianTree(i))
    utopianTree(2)