from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# // Solution of odd even
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        odd_head = head
        even_head = head.next

        while odd_head and odd_head.next:
            odd_head.next = odd_head.next.next
        odd_head.next = even_head
        while even_head and even_head.next:
            even_head.next = even_head.next.next

        return head
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
    ls = [1,1,2]
    head = create_linked_list(ls)

    head = Solution().oddEvenList(head)
    while head:
        print(head.val)
        head = head.next