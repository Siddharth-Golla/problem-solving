"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below,
determine the number of apples and oranges that land on Sam's house.

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range[s,t] )?

For example, Sam's house is between s=7 and t=10. The apple tree is located at a = 4 and the orange at b = 12. 
There are m = 3 apples and n = 3 oranges. Apples are thrown apples = [2,3,-4] units distance from a,
and oranges = [3,-2,-4] units distance from b. Adding each apple distance to the position of the tree, they land at [4+2, 4+3, 4+-4] = [6,7,0]. 
Oranges land at [12 + 3, 12+-2, 12+-4] = [15,10,8]. One apple and two oranges land in the inclusive range 7-10 so we print
1
2

"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count, oranges_count = 0,0
    for d in apples:
        landing_spot = a + d
        if (landing_spot) > a and (landing_spot >= s and landing_spot <= t):
            apples_count = apples_count + 1
    
    for d in oranges:
        landing_spot = b + d
        if landing_spot < b and (landing_spot <= t and landing_spot >= s):
            oranges_count = oranges_count + 1
    
    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    apples = [2, 3, -4]
    oranges = [3, -2, -4]
    countApplesAndOranges(7, 10, 4, 12, apples, oranges)
