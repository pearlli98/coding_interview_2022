question: https://leetcode.com/problems/insert-interval/submissions/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # append all the intervals that starts before newInterval
        # when we get to newInterval, append if no overlap, otherwise merge
        # append everything after, check for overlap each time
        # O(n)
        
        n = len(intervals)
        index = 0 
        output = []
        while index < n and intervals[index][0] < newInterval[0]:
            output.append(intervals[index])
            index += 1
            
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(newInterval[1], output[-1][1])
        
        while index < n:
            if output[-1][1] < intervals[index][0]:
                output.append(intervals[index])
            else:
                output[-1][1] = max(intervals[index][1], output[-1][1])
            index += 1
        
        return output
        
