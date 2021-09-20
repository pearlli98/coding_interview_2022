problem: https://leetcode.com/problems/merge-k-sorted-lists/solution/

sol: uses min heap bascially, but priority queue deals with objects? seems like

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # bascially uses a min heap 
        # https://stackoverflow.com/questions/18993269/difference-between-priority-queue-and-a-heap
        # O(N log k) where N is total number of nodes, k is number of lists 
        # O(1) get min from queue
        # O(log k) to insert and pop
        
        resultHead = result = ListNode(0)
        
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
                
        while not q.empty():
            val, currentNode = q.get()
            
            result.next = ListNode(val)
            result = result.next
            
            currentNode = currentNode.next
            if currentNode:
                q.put((currentNode.val, currentNode))
                
        return resultHead.next
