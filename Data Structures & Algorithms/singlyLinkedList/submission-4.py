class LinkNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = LinkNode(-1)
        self.tail = self.head

        

    def get(self, index: int) -> int:

        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = LinkNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode

        
        

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkNode(val)
        self.tail = self.tail.next

        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while i < index and curr.next:
            curr = curr.next
            i += 1

        if not curr.next:
            return False

        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res