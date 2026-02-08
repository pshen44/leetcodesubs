class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : Node(key, val)

        self.head = Node(-1, -1) #MOST REC USED
        self.tail = Node(-1, -1) #LEAST REC USED
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def insert(self, node):
        NXT = self.head.next
        self.head.next = node
        node.next = NXT
        NXT.prev = node
        node.prev = self.head

    def remove(self,node):
        PRV = node.prev
        NXT = node.next
        NXT.prev = PRV
        PRV.next = NXT

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if self.capacity < len(self.cache):
            LRU = self.tail.prev
            delkey = LRU.key
            del self.cache[delkey]
            self.remove(LRU)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
