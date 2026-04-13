class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = float('inf')
        for i, n in enumerate(nums):
            if n == target:
                min_dist=min(min_dist,abs(i - start))
        return min_dist

        