def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    num_list = []
    max_val(t)
    for i in t:
        if type(i) == int:
            num_list.append(i)
            # print(num_list)
        elif type(i) == tuple:
            for j in i:
                if type(j) == int:
                    num_list.append(j)
                elif type(j) == list:
                    num_list.append(j[0])
                else:
                    for l in j:
                        num_list.append(l)
                    # print(j)
                # if type(j) == tuple:
                #     num_list.append(j[0])
                # print(j)
                # print(num_list)
        else:
            for k in i:
                if type(k) == list:
                    num_list.append(k[0])
                elif type(k) == int:
                    num_list.append(k)
                else:
                    num_list.append(k)

                    # print(k[0])
                    # print(num_list)
    # print(num_list)
    # print(max(num_list))
    return max(num_list)


# max_val((5, (123, 2), [[1], [24]]))
max_val((-5, [6], ((3, 14), (5, 6)), (1, 2), [[12], [12]], [11, 11]))
# max_val((5, (1,2), [[1],[9]]))
