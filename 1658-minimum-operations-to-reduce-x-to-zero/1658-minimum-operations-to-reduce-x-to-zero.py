class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        # If x is greater than the total sum, it is impossible.
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        longest = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window until the sum is at most target.
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # We found a valid middle subarray.
            if current_sum == target:
                longest = max(longest, right - left + 1)

        # No subarray with the required sum exists.
        if longest == -1:
            return -1

        return len(nums) - longest