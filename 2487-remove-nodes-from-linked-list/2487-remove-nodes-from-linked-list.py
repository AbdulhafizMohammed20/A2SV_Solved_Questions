# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        
        
        max_val = float('-inf')
        dummy = ListNode(0)
        tail = dummy
        current = head
        while current:
            if current.val >= max_val:
                tail.next = current
                tail = current
                max_val = current.val
            current = current.next
        
        tail.next = None  
        
        prev = None
        current = dummy.next
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        return prev
