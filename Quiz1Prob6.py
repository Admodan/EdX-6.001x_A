def flatten(aList):
    newList = []
    for i in  range(len(aList)):
        if isinstance(aList[i], list):
            newList.extend(flatten(aList[i]))
        else:
            newList.append(aList[i])
    return newList
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]