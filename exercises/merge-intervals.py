question: https://leetcode.com/problems/merge-intervals/submissions/

sol: sort first and add each to output O(nlogn)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        output = [intervals[0]]
        index = 1
        while index < len(intervals):
            if intervals[index][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[index][1])
            else:
                output.append(intervals[index])
            index += 1
        return output
                
