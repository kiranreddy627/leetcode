/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node Dummy=new Node(-1);
        Node tail=Dummy;
        HashMap<Node,Node>hm=new HashMap<>();
        Node curr=head;
        while(curr!=null){
            int value=curr.val;
            Node nn=new Node(value);
            tail.next=nn;
            hm.put(curr,nn);
            curr=curr.next;
            tail=tail.next;
        }
        curr=head;
        hm.put(null,null);
        while(curr!=null){
            Node temp=hm.get(curr);
            Node templst=hm.get(curr.random);
            temp.random=templst;
            curr=curr.next;
        }
        return Dummy.next;
}
}