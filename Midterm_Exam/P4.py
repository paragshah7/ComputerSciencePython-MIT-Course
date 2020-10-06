def lessThan4(aList):
    """ aList: a list of strings """

    sList = []
    for value in aList:
        if len(value) < 4:
            sList.append(value)
    # print(sList)
    return sList


# aList = ["apple", "cat", "dog", "banana"]
# lessThan4(aList)
a = lessThan4(['PNCKqBX', 'hdyG', 'rw', 'QcWrLVPm', 'AxsL', '', 'uBXPFBh', 'LznYpLF'])
print(a)
