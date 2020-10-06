s = 'azcbobobegghakl'
count = 0
# for x in s:
#     if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#         count = count + 1

for index in range(len(s)):
    if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
        count = count + 1
print('Number of vowels:', count)
