# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        prev = None
        curr = head
        
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


list = [1,2,3,4,5,6,7,8]
head = list_to_linked_list(list)

# Delete the middle node
solution = Solution()
new_head = solution.reverseList(head)


print(linked_list_to_list(new_head))
