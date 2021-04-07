def search_bitonic_arr(nums, target):
    mid = (len(nums) - 1)//2
    if nums[mid] == target:
        return True
    if mid > 0: 
        left_adj = nums[mid-1]
        # Case 1: mid on asc slope, peak and target to right
        if left_adj < nums[mid] and nums[mid] < target:
            return search_bitonic_arr(nums[mid + 1:], target)
        # Case 2: mid on desc slope, target and peak to left
        if left_adj > nums[mid] and nums[mid] < target:
            return search_bitonic_arr(nums[:mid], target)
        # Case 3: target could be left or right 
        if nums[mid] > target:
            search_left = b_search_asc(nums[:mid], target)
            if search_left:
                return search_left
            else:
                return b_search_desc(nums[mid + 1:], target)
        
    # handling edge cases: if mid == 0, len(nums) is 2 or 1. Just manually check both I guess.
    if len(nums) == 1:
        return nums[mid] == target
    else:
        return nums[mid] == target or nums[mid + 1] == target 

def b_search_asc(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if nums[mid] == target:
            # return True
            return mid
        if nums[mid] < target:
            lo = mid + 1
        if nums[mid] > target:
            hi = mid - 1
    return False


def b_search_desc(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if nums[mid] == target:
            # return True
            return mid
        if nums[mid] > target:
            lo = mid + 1
        if nums[mid] < target:
            hi = mid - 1
    return False