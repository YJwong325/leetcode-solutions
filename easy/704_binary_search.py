def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
        
    return -1

# version that obeys Singe Entry Single Exit
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    res = -1
    found = False

    while l <= r and not found:
        mid = (l + r) // 2

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            res = mid
            found = True

    return res