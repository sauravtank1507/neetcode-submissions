# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        temp = dummy
        right = head


        if not head.next:
            return None

        while n > 0:
            right = right.next
            n-=1

        while right:
            right = right.next
            temp = temp.next

        temp. next = temp.next.next

        return dummy.next