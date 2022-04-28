

class NumList:

    def __init__(self):
        self.__items = []


    def __add__(self, new_item):
        self.__items.append(new_item)
        return self

    def __sub__(self, item):
        self.__items.remove(item)
        return self


    def __iter__(self):
        #print("create the iterator")
        self.__current_iter = iter(self.__items)
        return self

    def __next__(self):
        #print("next iteration")
        return next(self.__current_iter)


    def __gt__(self, value):
        return [ item > value for item in self.__items ]

    def __getitem__(self, selector_list):
        selected_items = []
        for index, _ in enumerate(self.__items):
            if selector_list[index]:
                selected_items.append(self.__items[index])
        return selected_items

    def __len__(self):
        return len(self.__items)


nums = NumList()
nums += 2 
nums = nums + 4
nums = nums + 6
nums = nums + 8
nums += 10
nums = nums + 12

print(nums[nums > 6])
print(len(nums))
