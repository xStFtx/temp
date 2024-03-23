class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second_half = slow.next
        slow.next = None
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = second_half
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        second_half = prev
        
        # Step 3: Merge the first half and the reversed second half alternately
        first_half = head
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
