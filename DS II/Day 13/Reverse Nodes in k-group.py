class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head=M_head=ListNode()
        dummy_head.next=head
       # Calculate Length
        l=0
        t=head
        
        while t:
            l+=1
            t=t.next
            
        # Get multiple length of k
        l//=k
        
        while head and l:
            
            for _ in range(1,k):
                
                temp=head.next
                head.next=temp.next
                temp.next=M_head.next
                M_head.next=temp
                
            if head:
                M_head,head=head,head.next
            l-=1
        return dummy_head.next
