# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        prev=None
        nex=None
        tempL=head
        tempR=head
        last=None
        ls=None
        c=1
        if left==right:
            return head
        if left==1:
            tempL=head
        while(cur):
            if c==left-1:
                tempL=cur
                cur=cur.next
            elif c==left:
                last=cur
                prev=cur
                cur=cur.next
            elif c>left and c<=right:
                nex=cur.next
                cur.next=prev
                prev=cur
                if c==right:
                    tempR=cur
                    cur=nex
                    c+=1
                    break
                cur=nex
            else:
                cur=cur.next
            c+=1
        if c==right+1:
            tempL.next=tempR
            last.next=nex
        if left==1:
            return prev
        return head