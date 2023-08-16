class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        while(slow):
	        if slow.val == None:
		        return True
	        slow.val = None
	        slow = slow.next
        return False