class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        while i+1 < len(nums1) and j+1 < len(nums2):
            if nums1[i] + nums2[j] < nums1[i + 1] + nums2[j]:
                pass

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(Solution().kSmallestPairs(nums1, nums2, k)) 