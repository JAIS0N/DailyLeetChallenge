class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        lesser_count = 0
        target_count = 0
        x=[]
        for num in nums:
            if num < target:
                lesser_count += 1
            elif num == target:
                target_count += 1
        x=list(range(lesser_count, lesser_count + target_count))      
        return x