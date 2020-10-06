
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return i, j


nums_list = [2, 7, 12, 17]
user_input = 9
print(twoSum(nums_list, user_input))

# def twoSum(nums, target):
#     count = 0
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             # print(i, j, nums[i], nums[j])
#             count += 1
#             # print('Number of iterations:', count)
#             if nums[i]+nums[j] == target:
#                 return i, j
