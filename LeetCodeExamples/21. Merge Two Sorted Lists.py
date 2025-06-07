# TODO : Implement me...
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_values(self):
        result = ""

        ptr = self
        while ptr is not None:
            result += f"{ptr.val} -> "
            ptr = ptr.next

        print(result)


from typing import Optional


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ptr_list_1 = list1
        ptr_list_2 = list2

        merged_list_head = ListNode(val=-101)
        ptr_merged_list = merged_list_head

        while ptr_list_1 or ptr_list_2:

            if ptr_list_1 is None and ptr_list_2:
                ptr_merged_list.next = ptr_list_2
                break

            if ptr_list_2 is None and ptr_list_1:
                ptr_merged_list.next = ptr_list_1
                break

            if ptr_list_1.val <= ptr_list_2.val:
                ptr_merged_list.next = ptr_list_1
                ptr_list_1 = ptr_list_1.next

            else:
                ptr_merged_list.next = ptr_list_2
                ptr_list_2 = ptr_list_2.next

            ptr_merged_list = ptr_merged_list.next

        merged_list_head = merged_list_head.next
        return merged_list_head


l1 = [1, 2, 4]
l2 = [1, 3, 4]

c = ListNode(4)
b = ListNode(2)
a1 = ListNode(1)

b.next = c
a1.next = b

c = ListNode(4)
b = ListNode(3)
a2 = ListNode(1)

b.next = c
a2.next = b

a1.print_values()
a2.print_values()

result = Solution().mergeTwoLists(a1, a2)

print("result :")
result.print_values()
# assert result == [1, 1, 2, 3, 4, 4]
