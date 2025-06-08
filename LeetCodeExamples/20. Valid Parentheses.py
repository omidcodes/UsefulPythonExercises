
class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:

    def __init__(self):
        self.top = None
    
    def push(self , val):
        
        new_node = Node(val=val)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        
    def pop(self):
        
        if self.top is None:
            return None
        
        node_value = self.top.val
        self.top = self.top.next

        return node_value


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack_open = Stack()


        for char in s:
            if char in ('(', '{', '['):
                stack_open.push(char)
                continue
            
            if stack_open.top is None :
                 # e.g : ')' : close without open
                return False

            top_of_open_stack = stack_open.pop()
            if {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            }[top_of_open_stack] != char:
                return False

        if stack_open.top is not None:
            # Finally
            return False
            
        return True



test_cases = {
    '()[]{}' : True,
    "([])" : True,
    "(]" : False,
}

for key, val in test_cases.items():

    output = Solution().isValid(s=key)
    assert output == val , f"{key=} , {val=}"
