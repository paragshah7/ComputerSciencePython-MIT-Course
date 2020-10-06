# s = 'azcbobobegghakl'
s = 'pzemgcnmvtk'
old_count = 0
new_str = ''
for x in s:
    # for y in s[a:len(s)]:
    # print('Main string is =', s, 'with length =', len(s))
    a = 0
    # print('a = ', a)
    left = s[a]
    b = a + 1
    right = s[b]
    count = 1

    # As long as string is alphabetically arranged, get the count
    while left <= right and a < len(s)-1:
        count = count + 1
        a = a + 1
        # print('a = ', a)
        left = s[a]
        b = a + 1
        # print('b = ', b)
        if b < len(s):    # because index out of range exception occurs
            right = s[b]

    # Because we only want to print the largest string in console
    if count > old_count:
        max_count = count
        new_str = s[0:max_count]
        old_count = count
    # print('Old count -', old_count)
    # print('Count list is :', countList)
    # print('Longest String Count = ', count)
    # print('Fetched string is = ', s[0:count], '\n')
    # print('Length of b =', b, ' and Length of s =', len(s))

    # As long as b is less than the length, create new string excluding the previous ordered string
    if b < len(s):
        s = s[b:len(s)]
        if len(s) == 1:   # Handling case for last char if its not in the order
            break
    else:
        # print('Breaking from for loop')
        break
# print('Count list is :', countList)
print('Longest substring in alphabetical order is:', new_str)
# print('Program done')
