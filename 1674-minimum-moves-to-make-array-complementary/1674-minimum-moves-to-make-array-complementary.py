class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            total = a + b

            # Start with 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # 1 move range
            diff[low] -= 1
            diff[high + 1] += 1

            # 0 move at exact current sum
            diff[total] -= 1
            diff[total + 1] += 1

        ans = float("inf")
        moves = 0

        for s in range(2, 2 * limit + 1):
            moves += diff[s]
            ans = min(ans, moves)

        return ans
        