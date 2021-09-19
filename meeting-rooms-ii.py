https://leetcode.com/problems/meeting-rooms-ii/solution/

sol: min heap, open new meeting room if the min ending time of current rooms is later than start. Need to sort first, O(nlogn)

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        # print(intervals)
        meetingRooms = [intervals[0][1]]
        heapq.heapify(meetingRooms)
        
        index = 1
        
        while index < len(intervals):
            if heapq.nsmallest(1, meetingRooms)[0] <= intervals[index][0]:
                heapq.heapreplace(meetingRooms, intervals[index][1])
            else:
                heappush(meetingRooms, intervals[index][1])
            index += 1
        
        return len(meetingRooms)
