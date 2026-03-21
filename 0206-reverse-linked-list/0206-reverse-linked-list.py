# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next :
            return head


        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        values = values[::-1]
      
        new_head = ListNode(0)
        curr = new_head

        for i in range(len(values)) :
            curr.next = ListNode(values[i])
            curr = curr.next
           

        return new_head.next
        