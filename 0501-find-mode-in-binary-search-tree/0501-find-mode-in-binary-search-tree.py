# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root.left==None and root.right==None:
            return [root.val]
        def find(root):
            nonlocal res
            if root==None:
                return 
            else:
                res.append(root.val)
                if root.right:
                    find(root.right)
                if root.left:
                    find(root.left)
        find(root)
        d=defaultdict(int)
        for i in res:
            d[i]+=1
        maxi=max(list(d.values()))
        ans=[]
        for i in res:
            if maxi==d[i]:
                ans.append(i)
        return list(set(ans))