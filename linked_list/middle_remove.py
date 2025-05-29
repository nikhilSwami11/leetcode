# Definition for singly-linked list.
from typing import Optional

def list_to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Convert linked list to list (for easy output)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head

list = [1,3,4,7,1,2,6]
head = list_to_linked_list(list)

# Delete the middle node
solution = Solution()
new_head = solution.deleteMiddle(head)


print(linked_list_to_list(new_head))
    
    
        
    

