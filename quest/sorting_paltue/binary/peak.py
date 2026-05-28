from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n -1
        ans = 0
        while left < right:
            mid = left + (right - left) // 2
            # Check if we are on the ascending slope
            if arr[mid] < arr[mid + 1]:
                left = mid + 1  # Peak is to the right, discard mid
            else:
                right = mid
        return left

if __name__ == "__main__":
    # Todo
    arr = [0,1,0]
    print(Solution().peakIndexInMountainArray(arr))
    pass