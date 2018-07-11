# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        diff = 0
        
        if curA is None or curB is None:
            return None
        
        while curA.next is not None:
            lenA+=1
            curA = curA.next
        
        while curB.next is not None:
            lenB+=1
            curB = curB.next
        
        if curA != curB:
            return None
        
        if lenA > lenB:
            curA = headA
            curB = headB
            diff = lenA - lenB
        else:
            curA = headB
            curB = headA
            diff = lenB - lenA
        
        while diff > 0:
            curA = curA.next
            diff-=1
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA