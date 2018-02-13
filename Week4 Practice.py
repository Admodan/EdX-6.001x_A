def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    trueList = []
    for item in L:
        if f(item) == True:
            trueList.append(item)
    L[:] = trueList
    return len(L)
#Function f(s) defined for us. Use below to test.
#L = ['ass', 'hat', 'baoot', 'squeeze', 'squish', 'affirmation', '', 'nope', 'n', 'a']

def f(s):
    return 'a' in s

#Solution 2: Iterating the string from the end, then deleting False entries.
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    trueList = []
    for i in reversed(range(len(L))):
        # I use str(L[i]) in case there is a number in the list
        if f(str(L[i])) == False:
            del L[i]
    return len(L)
