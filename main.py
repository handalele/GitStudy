def removeDuplicates(nums):
    len1 = len(nums)
    i = 0
    j = 0
    while j < len1:
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i = i + 1
        j = j + 1
    print(nums)
    return i+1
if __name__ == '__main__':
    list1 = [1,1,2,3]
    print(removeDuplicates(list1))