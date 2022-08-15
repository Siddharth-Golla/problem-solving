"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
If it is not possible to buy both items, return -1.

Example
b = 60
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58.
Choose the latter as the more expensive option and return 58.
"""

def getMoneySpent(keyboards:list, drives:list, b:int):
    spendable = []          # List of sum of keyboard and drive lower than budget
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    for keyboard in keyboards:
        for drive in drives:
            cost = keyboard + drive
            if cost == b:
                return b
            elif cost < b:
                spendable.append(cost)
            else:
                pass
    
    
    if len(spendable) == 0:
        return -1
    else:
        return max(spendable)


if __name__ == '__main__':
    print(getMoneySpent([3,2],[5,2,8],10))
    print(getMoneySpent([4],[5],5))
    print(getMoneySpent([25,100,800,300],[249,359,499,1099],2000))
