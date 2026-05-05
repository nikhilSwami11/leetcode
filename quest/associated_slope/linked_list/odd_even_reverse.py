from typing import List, Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next : ListNode = next

# // Solution of odd even
class Solution(object):
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd_start = head
        even_start = head.next
        even_start_fix = even_start

        while odd_start.next and even_start.next:
            # iterate the odd pointer
            odd_start.next = even_start.next
            odd_start = odd_start.next

            # iterate the even pointer 
            even_start.next = odd_start.next
            even_start = even_start.next
        
        odd_start.next = even_start_fix
        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    
def create_linked_list(ls: List[int]):
    if len(ls) ==0:
        return None
    head = None
    prev = head

    for i,val in enumerate(ls):
        curr = ListNode(val)
        if i == 0:
            head = curr
            prev = head
        else:
            prev.next = curr
        prev = curr
    return head

        
if __name__ == "__main__":
    ls = [2,1,3,5,6,4,7]
    head = create_linked_list(ls)

    head = Solution().oddEvenList(head)
    while head:
        print(head.val)
        head = head.next
