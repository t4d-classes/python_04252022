
nums = [1,2,3,4,5]

# imperative code - what you want, how to do what you want

# for (int x=0; x<len(nums); x++):
#     print(nums[x])

# very unpythonic.... never ever write this code...
# count = len(nums)
# counter = 0

# while counter < count:
#     print(nums[counter])
#     counter = counter + 1


# # declarative code - what you want

# # very pythonic
# for num in nums:
#     print(num)


def double(x):
    print("called double num")
    return x * 2

# uses a list to do a map
# def transform_list_items(transform_fn, items):

#     new_items = []

#     for item in items:
#         new_items.append(transform_fn(item))

#     return new_items

def transform_list_items(transform_fn, items):
    for item in items:
        yield transform_fn(item)



double_nums = transform_list_items(double, nums)
print(nums)
print(double_nums)

# for double_num in double_nums:
#     print(double_num)