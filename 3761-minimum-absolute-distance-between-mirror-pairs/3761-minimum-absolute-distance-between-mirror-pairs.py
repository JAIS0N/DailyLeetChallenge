class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_index = {}
        ans = float('inf')

        for j, num in enumerate(nums):
            if num in last_index:
                ans = min(ans, j - last_index[num])

            rev = self.reverse(num)
            last_index[rev] = j

        return -1 if ans == float('inf') else ans

    def reverse(self, x):
        rev = 0
        while x > 0:
            rev = rev * 10 + (x % 10)
            x //= 10
        return rev