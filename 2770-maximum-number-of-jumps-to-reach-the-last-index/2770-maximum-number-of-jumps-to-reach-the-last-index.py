class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i == n - 1:
                return 0

            if i in memo:
                return memo[i]

            best = float("-inf")

            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    result = dfs(j)

                    if result != float("-inf"):
                        best = max(best, 1 + result)

            memo[i] = best
            return best

        ans = dfs(0)
        return ans if ans != float("-inf") else -1