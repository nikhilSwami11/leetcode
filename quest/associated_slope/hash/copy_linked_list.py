# Definition for singly-linked list.


from typing import List, Optional


class Node(object):
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_new[curr]

            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]
            

def create_linked_list(ls: List[int]):
    if len(ls) ==0:
        return None
    head = None
    prev = head

    for i,val in enumerate(ls):
        curr = Node(val)
        if i == 0:
            head = curr
            prev = head
        else:
            prev.next = curr
        prev = curr
    return head

        
if __name__ == "__main__":
    ls = [1,2,3]
    head = create_linked_list(ls)

    head = Solution().copyRandomList(head)
    while head:
        print(head.val)
        head = head.next
    