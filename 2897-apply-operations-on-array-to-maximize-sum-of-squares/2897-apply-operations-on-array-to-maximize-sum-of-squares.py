class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31

        for num in nums:
            for bit in range(31):
                bit_counts[bit] += (num >> bit) & 1

        answer = 0

        for _ in range(k):
            value = 0
            for bit in range(31):
                if bit_counts[bit] > 0:
                    value |= 1 << bit
                    bit_counts[bit] -= 1
            answer = (answer + value * value) % MOD

        return answer