s = 'obobbbobobkbo'
value = 'bob'
j = len(value)
count = 0
find = ''
# a = 0
# for x in s:
#     b = a + 3
#     find = s[a:b]
#     if value == find:
#         count = count + 1
#     a = a + 1
for x in range(len(s)-(j-1)):
    j = len(value)
    while j > 0:
        find = find + s[len(value)-j+x]
        j = j - 1
    print(find)
    if value == find:
        count = count + 1
    find = ''
print('Number of times bob occurs is:', count)
