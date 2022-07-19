"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. 
Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Example
'2bbbb'
This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is 2.

'2bb#A'
This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is 1.

"""

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    has_numbers = False
    has_lower = False
    has_upper = False
    has_special = False
    result = 0
    for char in password:
        if char in numbers and has_numbers == False:
            result += 1
            has_numbers = True
        if char in lower_case and has_lower == False:
            result += 1
            has_lower = True
        if char in upper_case and has_upper == False:
            result += 1
            has_upper = True
        if char in special_characters and has_special == False:
            result += 1
            has_special = True
    
    required_type = 4 - result
    if n > 5:
        return required_type
    else:
        return max(6 - n,required_type)

if __name__ == '__main__':
    print(minimumNumber(1,"1"))
    print(minimumNumber(1,"%"))
    print(minimumNumber(2,"Ab"))
    print(minimumNumber(2,"be"))
    print(minimumNumber(3,"Ab1"))
    print(minimumNumber(3,"%$#"))
    print(minimumNumber(4,"abhi"))
    print(minimumNumber(4,"Al3$"))
    print(minimumNumber(5,"specl"))
    print(minimumNumber(5,"Sp3&s"))
    print(minimumNumber(6,"Sp3aR&"))
    print(minimumNumber(9,"imspecial"))