"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: (interval[0], interval[1]))
        
        index = 0
        
        while index < len(intervals) and len(intervals) != 1 and index != len(intervals)-1:
            [current_start, current_end] = intervals[index]
            [next_start, next_end] = intervals[index+1]
            
            if current_start in range(next_start, next_end+1):
                new_start = next_start
                new_end = max(current_end, next_end)
                
                intervals.pop(index)
                intervals.pop(index) # Actually index+1
                
                intervals.insert(index, [new_start, new_end])
            elif next_start in range(current_start, current_end+1):
                new_start = current_start
                new_end = max(current_end, next_end)
                
                intervals.pop(index)
                intervals.pop(index) # Actually index+1
                
                intervals.insert(index, [new_start, new_end])
            else:
                index += 1
        
        return intervals