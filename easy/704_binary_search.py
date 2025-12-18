def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        # mid = (l + r) // 2
        mid = l + (r - l) // 2
        
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
        
    return -1

# version that obeys Singe Entry Single Exit
def binary_search2(nums, target):
    l, r = 0, len(nums) - 1
    res = -1
    found = False

    while l <= r and not found:
        # mid = (l + r) // 2
        mid = l + (r - l) // 2

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            res = mid
            found = True

    return res

# test for version 1
num_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
print("-" * 60)
print("Example array 1:", num_array)
print("The index found for the number", target, "is", binary_search(num_array, target))

target = 8
print("The index found for the number", target, "is", binary_search(num_array, target))

# test for version 2 (Obeys SESE)
num_array_2 = [3, 8, 12, 17, 23, 28, 34, 39, 45, 50]
target = 3
print("-" * 60)
print("Example array 2:", num_array_2)
print("The index found for the number", target, "is", binary_search2(num_array_2, target))

target = 24
print("The index found for the number", target, "is", binary_search2(num_array_2, target))
print("-" * 60)
