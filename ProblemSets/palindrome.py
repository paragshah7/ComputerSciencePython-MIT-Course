num = 12121
x = 0
res = [int(x) for x in str(num)]
print("The list from number is " + str(res))
if len(res) % 2 == 0:
    print('Even digits')
for i in range(int((len(res))/2)):
    if res[i] == res[len(res)-i-1]:
        print('Hi')
    else:
        print('Palindrome')
        break
