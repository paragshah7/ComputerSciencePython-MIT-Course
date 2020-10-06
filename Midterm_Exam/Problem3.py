def sum_digits(s):
    sum = 0
    typec = 0
    for value in s:
        # print(type(value))
        # print(value)
        try:
            new_int = int(value)
            # print(type(new_int))
        except Exception as E:
            new_int = 'Assigning string type'
        if type(new_int) == int:
            sum = sum + new_int
            # print('Sum =', sum)
    # print(sum)
    if sum == 0:
        raise ValueError
    return sum


sum_digits('sds1')
