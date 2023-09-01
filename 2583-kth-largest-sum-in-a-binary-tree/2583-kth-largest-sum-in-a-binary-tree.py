# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        op=[]
        lst=[]
        qu=[]
        d=[]
        qu.append(root)
        if root == None:
            return op
        op.append(root.val)
        while(qu):
            while(qu):
                cur=qu.pop(0)
                if cur.left:
                    lst.append(cur.left)
                    d.append(cur.left.val)
                if cur.right:
                    lst.append(cur.right)
                    d.append(cur.right.val)
            if d:
                op.append(sum(d))
            qu=lst
            lst=[]
            d=[]
        op.sort()
        if len(op)<k:
            return -1
        return op[-k]