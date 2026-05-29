class Solution(object):
    def minElement(self, nums):
        minimum_value = float('inf')

        for number in nums:
            digit_sum = 0

            while number > 0:
                digit_sum = digit_sum + (number % 10)
                number = number // 10

            minimum_value = min(minimum_value, digit_sum)

        return minimum_value