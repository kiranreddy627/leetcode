"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        lst=[]
        qu=[]
        if not root:
            return None
        root.next=None
        qu.append(root)
        while(qu):
            while(qu):
                cur=qu.pop(0)
                if cur.left:
                    lst.append(cur.left)
                if cur.right:
                    lst.append(cur.right)
            if lst:
                prev=None
                for i in lst[::-1]:
                    i.next=prev
                    prev=i
            qu=lst
            lst=[]
        return root