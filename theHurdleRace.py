"""
A video player plays a game in which the character competes in a hurdle race.
Hurdles are of varying heights, and the characters have a maximum height they can jump.
There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose.
How many doses of the potion must the character take to be able to jump all of the hurdles.
If the character can already clear all of the hurdles, return 0.

Example
height = [1,2,3,3,2]
k = 1

The character can jump 1 unit high initially and must take 3 - 1 = 2 doses of potion to be able to jump all of the hurdles.
"""

def hurdleRace(k, height):
    maximum_height = max(height)
    if k >= maximum_height:
        return 0
    else:
        return maximum_height - k

if __name__ == '__main__':
    print(hurdleRace(4, [1,6,3,5,2]))
    print(hurdleRace(7, [2,5,4,5,2]))
