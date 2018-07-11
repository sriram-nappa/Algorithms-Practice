# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current:
            runner = current.next
            while runner and runner.val == current.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next =  ListNode(1), ListNode(2)
    head.next.next.next = ListNode(3)
    print(Solution().deleteDuplicates(head))