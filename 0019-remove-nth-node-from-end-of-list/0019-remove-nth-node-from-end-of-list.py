# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  # Create a dummy node pointing to head
        # This helps handle edge cases (like removing first node)
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy

        # --------------------------------------------------
        # STEP 1: Move fast n+1 steps ahead
        # --------------------------------------------------
        for _ in range(n + 1):
            fast = fast.next

        # --------------------------------------------------
        # STEP 2: Move both pointers together
        # --------------------------------------------------
        while fast:
            slow = slow.next
            fast = fast.next

        # --------------------------------------------------
        # STEP 3: Delete the node
        # --------------------------------------------------
        # slow is just before the node to delete
        slow.next = slow.next.next

        return dummy.next
        
        