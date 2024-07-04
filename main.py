# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Initialize a dummy node to help with the new list
        dummy = ListNode(0)
        current_new_list = dummy
        
        current = head.next  # Skip the first zero
        current_sum = 0
        
        while current:
            if current.val == 0:
                # We encountered a zero, means we end the current segment
                if current_sum > 0:
                    # Create a new node with the accumulated sum and reset sum
                    current_new_list.next = ListNode(current_sum)
                    current_new_list = current_new_list.next
                    current_sum = 0
            else:
                # Accumulate the values between zeros
                current_sum += current.val
            
            current = current.next
        
        return dummy.next

