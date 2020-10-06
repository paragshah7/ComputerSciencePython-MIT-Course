def uniqueValues(aDict):
    """ aDict: a dictionary """

    # keysList = []
    # valuesList = []
    #
    # uniqueVal = list(set(aDict.values()))
    # print(uniqueVal)
    #
    # for i in aDict:
    #     print(i, aDict[i])
    #     if aDict[i] not in valuesList:
    #         keysList.append(i)
    #     valuesList.append(aDict[i])
    # # print(sorted(keysList))
    # print('Ans is -', keysList)
    # print(valuesList)

    # print(aDict.values())
    newDict = {}
    # print(newDict)
    for key, value in aDict.items():
        if value not in newDict.keys():
            newDict[value] = [key, 1]
        else:
            newDict[value][1] += 1
            # counter = counter + 1
            # newDict[value][1] = counter

    # print(newDict)
    keysList = []
    for key, value in newDict.items():
        if value[1] == 1:
            keysList.append(value[0])

    return sorted(keysList)
        # for i in aDict:
    #     if aDict[i] not in newDict:
    #         newDict = aDict.values(0)


uniqueValues({1: 4, 2: 5, 3: 6, 4: 20, 5: 20, 6: 4})
