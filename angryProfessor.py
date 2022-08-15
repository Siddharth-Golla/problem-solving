"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
the professor decides to cancel class if fewer than some number of students are present when class starts.
Arrival times go from on time (arrivalTime =< 0) to arrived late (arrivalTime > 0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

Example
n = 5
k = 3
a = [-2,-1,0,1,2]

The first 3 students arrived on time. The last 3 were late. The threshold is 3 students, so class will go on. Return YES.
"""

def angryProfessor(k:int, a:list):
    students_ontime = 0
    for student in a:
        if student <= 0:
            students_ontime += 1
    if students_ontime >= k:
        return "NO"
    else:
        return "YES"

    


if __name__ == '__main__':
    threshold = 3
    a = [-2,-1,0,3,2]
    b = [-1, -3, 4, 2]
    print(angryProfessor(threshold, a))
    print(angryProfessor(threshold, b))
    print(angryProfessor(2,[0, -1, 2, 1]))
