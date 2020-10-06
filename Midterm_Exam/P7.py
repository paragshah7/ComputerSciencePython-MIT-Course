
def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    # print(L)
    # for i in L:
    #     # print('i =', i)
    #     test = g(f(i))
    #     # print('**********', test)
    #     if test == False:
    #         L.remove(i)
    #         # L = L[1:len(L)]
    #         # print(L)
    #     # else:
    #         # print(L)
    #         # i = i-1
    #         # print(L.remove())
    # L.pop(0)
    # return max(L)

    arrLength = len(L)
    i = 0
    while i < arrLength:
        # print(i, L[i], g(f(L[i])))
        evaluation = g(f(L[i]))
        # print(i, evaluation)
        if not evaluation:
            L.pop(i)
            arrLength = len(L)
            # continue
        else:
            i = i + 1

    if len(L) == 0:
        return -1
    else:
        return max(L)


L = []
print(applyF_filterG(L, f, g))
print(L)
