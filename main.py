# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = reverseLinkedList(slow)
        
        # Compare the first and second halves
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True