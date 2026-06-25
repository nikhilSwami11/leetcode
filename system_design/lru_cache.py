class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key     
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.max_len = capacity
        self.mp = {}   
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node):
        # Insert node right between dummy head and the real first node
        old_first = self.head.next
        
        node.prev = self.head
        node.next = old_first
        
        self.head.next = node
        old_first.prev = node
        
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            new_node = Node(key, value)
            self.mp[key] = new_node
            self._add_to_head(new_node)
            
            if len(self.mp) > self.max_len:
                victim = self.tail.prev
                self._remove(victim)
                del self.mp[victim.key]  