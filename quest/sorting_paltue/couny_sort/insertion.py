from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Your code will go here!

        curr = head.next
        dummy = ListNode(0)

        while curr:
            next_unsorted = curr.next
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            # Splice 'curr' into its sorted position between 'prev' and 'prev.next'
            curr.next = prev.next
            prev.next = curr
            
            # Move on to the next unsorted node we saved earlier
            curr = next_unsorted
            
        return dummy.next


# ==========================================
# Helper functions to test your code locally
# ==========================================

def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Helper to convert a standard Python list into a Linked List."""
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head: Optional[ListNode]):
    """Helper to cleanly print your linked list values."""
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals) if vals else "Empty List")

# Test Case Execution
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: Unsorted list [4, 2, 1, 3]
    input_array = [4, 2, 1, 3]
    head = create_linked_list(input_array)
    
    print("Original List:")
    print_linked_list(head)
    
    # Call your sorting function
    sorted_head = solution.insertionSortList(head)
    
    print("\nSorted List:")
    print_linked_list(sorted_head)