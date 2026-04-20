# Definition for singly-linked list.


from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        
        prev = head
        curr = head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
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

    head = Solution().deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next
    