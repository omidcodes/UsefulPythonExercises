
# TODO : Implement me...
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# from typing import Optional
#
#
# class Solution:
#
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         pass
#
#
# l1 = [1, 2, 4]
# l2 = [1, 3, 4]
#
# c = ListNode(4)
# b = ListNode(2)
# a1 = ListNode(1)
#
# b.next = c
# a1.next = b
#
# c = ListNode(1)
# b = ListNode(3)
# a2 = ListNode(4)
#
# b.next = c
# a2.next = b
#
# result = Solution().mergeTwoLists(a1, a2)
#
# while result is not None:
#     print(result.val)
#     result = result.next
#
# # assert result == [1, 1, 2, 3, 4, 4]
