from random import randint

# nums = []

# for num in range(10):
#     nums.append(randint(0, 100))

nums = [ randint(0, 100) for _ in range(10) ]

print(nums)

# nums.sort()
# print(nums)

sorted_nums = sorted(nums, reverse=True)

print(nums)
print(sorted_nums)
