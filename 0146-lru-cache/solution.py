class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node(key, value)

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    def insert(self, node):
        prvnode = self.tail.prev
        nxtnode = self.tail
        node.next = nxtnode
        node.prev = prvnode
        prvnode.next = node
        nxtnode.prev = node

    def remove(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            # {1 : 1}
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.head.next
            self.remove(LRU)
            del self.cache[LRU.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
