class ListNode {
    constructor(x) {
        this.val = x;
        this.next = null; 
    }
}

hasCycle = (head) => {
    let fast = head;
    let slow = head;
    while(fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
        if(fast == slow) {
            return true;
        }
    }
    return false;
}

let head = new ListNode(2)
head.next = new ListNode(3)
head.next.next = new ListNode(4)
head.next.next.next = head
console.log(hasCycle(head))