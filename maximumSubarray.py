def maxSubArray(nums: list[int]) -> int:
    # Self thought code, also found it is known as Kadane's Algorithm
    maximum = curr_max = nums[0]

    for num in nums[1:]:
        # This will replace smaller sum by val, if val>sum
        curr_max = max(num, num + curr_max)
        maximum = max(maximum, curr_max)

    return maximum
