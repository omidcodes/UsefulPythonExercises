
class Node:

    def __init__(self, val, next = None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev    

    # def __repr__(self):
    #     return f"{self.val=} "
    
class DLL:

    def __init__(self, head):
        self.head = head
        self.tail = head

    def __repr__(self):
        return f"{self.head=} {self.head=}"

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """

        __homepage_node = Node(val=homepage)
        self.homepage = DLL(head=__homepage_node)
        self.cur = __homepage_node

    def print_values(self):
        curr = self.homepage.head

        vals = ""
        while curr:
            vals+=f"{curr.val} -> "
            curr = curr.next

        return vals


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """


        new_site_node = Node(val=url, next=None, prev=self.cur)

        self.cur.next = new_site_node
        self.cur = self.cur.next    # sets the current cursor to newly visited site
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        for _ in range(steps):
            if self.cur.prev is None:
                break
            self.cur = self.cur.prev
        
        return self.cur.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """


        for _ in range(steps):
            if self.cur.next is None:
                break
            self.cur = self.cur.next
        
        return self.cur.val




obj = BrowserHistory(homepage="icpbj.com")


input_list = [[1],[10],["xbepk.com"],[8],["kls.com"],["dlkwxpf.com"],["pnep.com"],[9],["rmis.com"],["bxf.com"],["dz.com"],[2],["acuqsax.com"],["dcvo.com"],["ijbg.com"],["nlott.com"],[7],["dd.com"],["vssnq.com"],["teur.com"],["pn.com"],["szi.com"],["brhldg.com"],["yulyoqv.com"],[4],[10],[8],[5],["av.com"],[3],["okr.com"],["meli.com"]]
func_list = ["back","back","visit","forward","visit","visit","visit","back","visit","visit","visit","back","visit","visit","visit","visit","back","visit","visit","visit","visit","visit","visit","visit","back","forward","back","forward","visit","back","visit","visit"]
expected_list = ["icpbj.com","icpbj.com",None,"xbepk.com",None,None,None,"icpbj.com",None,None,None,"rmis.com",None,None,None,None,"icpbj.com",None,None,None,None,None,None,None,"teur.com","yulyoqv.com","icpbj.com","szi.com",None,"teur.com",None,None]

for func, input, expected in zip(func_list, input_list, expected_list):
    output = getattr(obj,func)(input[0])
    print(f"{func=} , {input[0]=} -> {output=} , |||| {obj.cur.val=} , DEBUG=== {obj.print_values()=} \n\n")
    assert output == expected, f"WRONG ----> {expected=} , {output=}"

print("test passed")
