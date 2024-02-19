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

        pointer_list_1 = list1
        pointer_list_2 = list2

        merged_list_head = ListNode(val=-101)
        pointer_merged_list = merged_list_head

        while pointer_list_1 or pointer_list_2:

            # merged_list_head.print_values()
            # print("-----")

            if pointer_list_1 is None and pointer_list_2:
                pointer_merged_list.next = pointer_list_2
                break

            if pointer_list_2 is None and pointer_list_1:
                pointer_merged_list.next = pointer_list_1
                break

            if pointer_list_1.val <= pointer_list_2.val:
                pointer_merged_list.next = pointer_list_1
                pointer_list_1 = pointer_list_1.next

            else:
                pointer_merged_list.next = pointer_list_2
                pointer_list_2 = pointer_list_2.next

            pointer_merged_list = pointer_merged_list.next

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
