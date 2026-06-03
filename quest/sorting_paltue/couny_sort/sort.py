from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        def max_heapify(size: int, root_idx: int):
            largest = root_idx
            left_child = 2 * root_idx + 1
            right_child = 2 * root_idx + 2

            # Check if left child exists and is larger than root
            if left_child < size and nums[left_child] > nums[largest]:
                largest = left_child

            # Check if right child exists and is larger than the largest so far
            if right_child < size and nums[right_child] > nums[largest]:
                largest = right_child

            # If the largest element is not the root, swap and continue heapifying
            if largest != root_idx:
                nums[root_idx], nums[largest] = nums[largest], nums[root_idx]
                max_heapify(size, largest)

        # Step 1: Build a Max-Heap out of the input array.
        # We start from the last non-leaf node and work backward.
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)

        # Step 2: Extract elements from the heap one by one.
        # Move the current largest element (at index 0) to the end of the array.
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Swap root with last element
            max_heapify(i, 0)                   # Re-heapify the reduced heap

        return nums

nums = [5,2,3,1]
Solution().sortArray(nums)
