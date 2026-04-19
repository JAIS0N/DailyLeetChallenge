class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # nums2[j] too small for nums1[i]; need smaller nums1[i]
                i += 1
                j = max(j, i)  # enforce i <= j

        return max_dist