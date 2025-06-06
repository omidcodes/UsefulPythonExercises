# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False
        
        if head.next is None:
            return False
        
        slow_ptr = head
        fast_ptr = head

        while True:

            if fast_ptr is None:
                return False

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

            if fast_ptr is None:
                return False
            
            fast_ptr = fast_ptr.next

            if slow_ptr == fast_ptr:
                return True
            