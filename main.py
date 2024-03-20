# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node before the ath node
        prev_a = None
        current = list1
        for _ in range(a):
            prev_a = current
            current = current.next
        
        # Find the node after the bth node
        prev_b = None
        for _ in range(b+1):
            prev_b = current
            current = current.next
        
        # Connect the nodes
        prev_a.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = prev_b
        
        return list1
