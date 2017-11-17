class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                return True
        return False

if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head
    print Solution().hasCycle(head)
