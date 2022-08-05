# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
	
        hashMap = {}
        temp = head
        while temp:
            if temp in hashMap:
                return temp
            else:
                hashMap[temp] = temp.val
            temp = temp.next
