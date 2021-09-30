question: https://leetcode.com/problems/non-overlapping-intervals/submissions/

sol: greedy solution
1. sort the intervals by start
2. if no overlap, append to output; 
   else (cur start < prev end)
	if cur end > prev end: choose previous
        if cur end < prev start: choose current

the point is: always choose the one with a smaller end to leave room for future intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy O(nlogn)
        intervals = sorted(intervals, key = lambda x:x[0])
        output = [intervals[0]]
        index = 1
        while index < len(intervals):
            if intervals[index][0] >= output[-1][1]:
                output.append(intervals[index])
            else:
                if intervals[index][1] < output[-1][1]:
                    output[-1] = intervals[index]
                else:
                    index += 1
        return len(intervals) - len(output)
        
