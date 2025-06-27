class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.right = Node(0)
        self.left = Node(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        i = 0
        curr = self.left.next
        while curr and curr != self.right:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_val = Node(val)
        nxt = self.left.next
        prv = self.left

        prv.next = new_val
        nxt.prev = new_val
        new_val.next = nxt
        new_val.prev = prv
        return


    def addAtTail(self, val: int) -> None:
        new_val = Node(val)
        nxt = self.right
        prv = self.right.prev

        prv.next = new_val
        nxt.prev = new_val
        new_val.next = nxt
        new_val.prev = prv
        return

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        new_val = Node(val)
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new_val = Node(val)
            nxt = curr
            prv = curr.prev

            prv.next = new_val
            nxt.prev = new_val
            new_val.next = nxt
            new_val.prev = prv
        return


    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            nxt = curr.next
            prv = curr.prev

            nxt.prev = prv
            prv.next = nxt
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
