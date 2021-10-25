https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        res = ListNode(0)
        p = l1
        q = l2
        cur = res
        carry = 0
        
        while p or q:
            if p:
                x = p.val
            else: x = 0
                
            if q:
                y = q.val
            else: y = 0
            s = x + y + carry
            carry = s / 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            
            if p: p = p.next
            if q: q = q.next
        if carry > 0:
            cur.next = ListNode(carry)
            
        return res.next