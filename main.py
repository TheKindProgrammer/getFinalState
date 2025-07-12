def getFinalState(nums, k, multiplier):
    while k > 0:
        val = min(nums)
        index = nums.index(val)
        nums[index] = val * multiplier
        k -= 1

    return nums