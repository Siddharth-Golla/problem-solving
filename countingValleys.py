"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps,
for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level,
and each step up or down represents a 1 unit change in altitude. 

We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example
steps = 8 path = [DDUUUUDD]

The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.
"""

def countingValleys(steps, path):
    result = 0
    position = 0
    for item in path:
        if item == "D":
            if position == 0:
                result = result + 1
            position = position - 1
        else:
            position = position + 1
        
    return result


if __name__ == '__main__':
    print(countingValleys(7,"UDDDUDUU"))
    print(countingValleys(9,"DUDUDUDUUDUD"))
    print(countingValleys(3,"UDDDDUUDUUUU"))
