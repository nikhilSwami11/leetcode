from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        curr_index = 0
        for i in range(len(intervals)-1):
            if merged_intervals[curr_index][1] < intervals[i+1][0]:
                # close interval
                merged_intervals.append(intervals[i+1])
                curr_index +=1
            else:
                merged_intervals[curr_index][1] = max(merged_intervals[curr_index][1], intervals[i+1][1])
        return merged_intervals

if __name__ == "__main__":
    intervals = [[4,7],[1,4]]
    print(Solution().merge(intervals))