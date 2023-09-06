# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lst,n,tmp=[],0,head
        while tmp:
            n+=1
            lst.append(tmp.val)
            tmp=tmp.next
        res,i,start=[],0,0
        while i<k:
            size,rem=n//k,n%k
            ele=size + (1 if rem else 0)
            n-=1
            lis=lst[start:start+ele]
            res.append(lis)
            start+=ele
            i+=1
        ans=[]
        for i in range(len(res)):
            temp=dummy=ListNode(0)
            for j in range(len(res[i])):
                temp.next=ListNode(res[i][j])
                temp=temp.next
            ans.append(dummy.next)
        return ans