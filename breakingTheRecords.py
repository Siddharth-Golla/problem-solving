"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
Example:
scores = [12,24,10,24]
Since she breaks the record for least score once and max score once
Output:
[1,1]

"""


def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    maxi_counter = 0
    mini_counter = 0
    for i in range(1,len(scores)):
        if scores[i] < minimum:
            minimum = scores[i]
            mini_counter = mini_counter + 1
        if scores[i] > maximum:
            maximum = scores[i]
            maxi_counter = maxi_counter + 1
        
    return [maxi_counter, mini_counter]

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    print(breakingRecords(scores))

