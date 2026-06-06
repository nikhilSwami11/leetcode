from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            print(slow.val,fast.val)
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        mid = prev
        max_sum = -1
        while slow:
            max_sum = max(max_sum,slow.val + mid.val)
            slow = slow.next
            mid = mid.next

        return max_sum


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
    
    # Example: Twin pairs are (5, 1) and (4, 2)
    # Expected Max Pair Sum: max(5+1, 4+2) = 6
    input_array = [5, 4, 2, 1]
    head = create_linked_list(input_array)
    
    print("Original List:")
    print_linked_list(head)
    
    # Call your function
    result = solution.pairSum(head)
    print(f"\nMaximum Twin Sum: {result}")