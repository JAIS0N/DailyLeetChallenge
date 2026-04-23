from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Group indices by value
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        
        arr = [0] * len(nums)
        
        for indices in groups.values():
            k = len(indices)
            if k == 1:
                continue
            
            # Build prefix sum of indices
            prefix = [0] * (k + 1)
            for m in range(k):
                prefix[m + 1] = prefix[m] + indices[m]
            
            total = prefix[k]  # sum of all indices in group
            
            for m, idx in enumerate(indices):
                left_sum = prefix[m]           # sum of indices[0..m-1]
                right_sum = total - prefix[m + 1]  # sum of indices[m+1..k-1]
                
                left_count = m
                right_count = k - 1 - m
                
                arr[idx] = (idx * left_count - left_sum) + (right_sum - idx * right_count)
        
        return arr
        