""" closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0 """
import sys


def closest_power(base, num):
    exponent = 0
    new_num = base ** exponent

    while new_num < num:
        exponent += 1
        new_num = base ** exponent

    min_exp = exponent - 1
    min_num = base ** min_exp
    max_exp = exponent
    max_num = base ** max_exp
    print(min_exp, min_num)
    print(max_exp, max_num)

    dist_min_num = num - min_num
    dist_max_num = max_num - num
    print(dist_min_num, dist_max_num)
    if dist_min_num < dist_max_num:
        return min_exp
    elif dist_min_num == dist_max_num:
        return min_exp
    else:
        return max_exp


# test_num = closest_power(4, 1)(2, 192.0)
test_num = closest_power(2, 192.0)
print(test_num)
