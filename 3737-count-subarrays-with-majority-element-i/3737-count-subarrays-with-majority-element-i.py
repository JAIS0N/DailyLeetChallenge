class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            count_target = 0

            for right in range(left, n):
                if nums[right] == target:
                    count_target += 1

                length = right - left + 1

                if count_target > length // 2:
                    ans += 1

        return ans
        