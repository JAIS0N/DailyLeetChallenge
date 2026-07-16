class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        prefix_max = 0

        for num in nums:
            prefix_max = max(prefix_max, num)
            prefix_gcd.append(gcd(num, prefix_max))

        prefix_gcd.sort()

        left = 0
        right = len(prefix_gcd) - 1
        total = 0

        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return total
        