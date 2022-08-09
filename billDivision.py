"""
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume.
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct. For example, assume the bill has the following prices: bill = [2,4,6].
Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2 + 4)/2 = 3. If he includes the cost of bill[2], he will calculate (2 + 4 + 6)/2 = 6.
In the second case, he should refund 3 to Anna.
"""

def bonAppetit(bill, k, b):
    bill_actual = (sum(bill) - bill[k])//2
    bill_charged = b
    if bill_charged > bill_actual:
        return print(bill_charged - bill_actual)
    if bill_charged == bill_actual:
        return print("Bon Appetit")


if __name__ == '__main__':
    bill = [3,10,2,9]
    k = 1
    b = 12
    bonAppetit(bill, k, b)
