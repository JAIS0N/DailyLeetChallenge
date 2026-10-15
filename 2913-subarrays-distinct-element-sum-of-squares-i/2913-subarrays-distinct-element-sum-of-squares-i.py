class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Iterate over all possible start points of subarrays
        for i in range(n):
            distinct_set = set()
            # Iterate over all possible end points of subarrays
            for j in range(i, n):
                distinct_set.add(nums[j])
                # Add the square of the distinct count for the current subarray
                total_sum += len(distinct_set) ** 2
                
        return total_sum
        