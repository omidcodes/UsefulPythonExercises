# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val=} , {self.next=}"


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return None

        # reversing
        prev = None
        current = head
        next = current.next

        while True:

            if current.next is None:
                current.next = prev
                head = current
                break

            current.next = prev
            prev = current
            tmp_next = next.next
            current = next
            next = tmp_next

        head = current

        return head
    

ll = [1,2,3,4,5]

ll_1 = ListNode(1)
ll_2 = ListNode(2)
ll_3 = ListNode(3)
ll_4 = ListNode(4)
ll_5 = ListNode(5)

ll_1.next = ll_2
ll_2.next = ll_3
ll_3.next = ll_4
ll_4.next = ll_5


s = Solution()

output = s.reverseList(head=ll_1)
print(output)