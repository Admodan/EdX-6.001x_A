#Many people have complained in the discussion that the/
# method with which they count steps seems to be flawed.
#Things like skipping the for loop if there is an empty list,/ 
# even though you still need to check the list is empty.
#Super useful website to step through code and see the variables/
# and environment: http://pythontutor.com/

#Problem 2
#For the worst and best case scenarios, fill in how many/
#steps it would take for the program to run.

def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

#Answer:
#Best case: = 2*1000 + 2
#Worst Case: 2+2*1000+3*n

def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x /= 2
        total += x

    return total

#Best Case:3+2*1000
#Worst Case: 5*log2(n) + 2008 
#Explanation: Doesn't go into infinite loop because only uses interger values/
#so 1/2 = 0. Use log2(n) to reduce n until its interger is 0. Log2(8) = 3.

def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)

#Best case:3. If the list is empty only the assignment statements and return/
#are executed.
#Worst case: 7*n + 2. 

#Problem 3:
#Fill in best case and worst case number of steps for each program below.
def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples
#Best case:2
#Wors case:3*n^2 + n + 2
#Explanation: https://courses.edx.org/courses/course-v1:MITx+6.00.1x_9+2T2016/
#courseware/0892c070e6464647bb8e9b9aa753d395/videosequence:Lecture_8/

def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares
#Best case:2
#Wors case:4*n^2 + n +2

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection
#Best case:2
#Wors case:n^2 + 2*n + 2