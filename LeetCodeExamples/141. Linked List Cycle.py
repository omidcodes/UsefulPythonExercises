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

        lst = [head]

        ptr = head

        while True:

            ptr = ptr.next
            if ptr is None:
                # LinkedList has end (no loop)
                return False
            
            lst.append(ptr)
            if len(lst) != len(set(lst)):
                # A node is seen two times -> loop
                return True
            