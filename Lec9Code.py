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