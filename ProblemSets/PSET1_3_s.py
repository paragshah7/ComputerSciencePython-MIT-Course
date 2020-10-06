s = 'pzemgcnmvtk'
old_count = 0
new_str = ''
for x in s:
    a = 0
    left = s[a]
    b = a + 1
    right = s[b]
    count = 1
    while left <= right and a < len(s) - 1:
        count = count + 1
        a = a + 1
        left = s[a]
        b = a + 1
        if b < len(s):
            right = s[b]
    if count > old_count:
        max_count = count
        new_str = s[0:max_count]
        old_count = count
    if b < len(s):
        s = s[b:len(s)]
        if len(s) == 1:
            break
    else:
        break
print('Longest substring in alphabetical order is:', new_str)
