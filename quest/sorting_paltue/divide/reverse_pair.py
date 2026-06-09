from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge(list1, list2):

            nonlocal count
            n = len(list1)
            m = len(list2)
            merge_arr = []
            i = 0
            j = 0
            p1= 0
            p2 = 0
            while p1 < n and p2 < m:
                if list1[p1] > 2 * list2[p2]:
                    # If true, all elements from p1 to the end of list1 are valid!
                    count += (n - p1)
                    p2 += 1  # Move list2 pointer forward
                else:
                    p1 += 1  # Move list1 pointer forward

            while i < n and j< m:
                if list1[i] < list2[j]:
                    merge_arr.append(list1[i])
                    i+=1
                else:
                    merge_arr.append(list2[j])
                    j+=1
            while i < n:
                merge_arr.append(list1[i])
                i+=1
            while j < m:
                merge_arr.append(list2[j])
                j+=1

            return merge_arr


        def mergeSort(nums: List[int]):
            n = len(nums)
            if n == 1:
                return nums
            
            arr1 = nums[0:n//2]
            arr2 = nums[(n//2):] 

            return merge(mergeSort(arr1),mergeSort(arr2))
        
        mergeSort(nums)
        
        return count

nums = [1,3,2,3,1]
print(Solution().reversePairs(nums))

