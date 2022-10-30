import pep8 # noqa

def Remove_Duplicates(nums):
    count = 0
    last = None
    for i in range(len(nums)
    ):
        if nums[i] == last:
            continue
        else:
            last = nums[i]
            nums[count] = nums[i]
            count+= 1   
    return count


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Remove_Duplicates(nums))