class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            val = node.value
            self.remove(node)
            self.insert(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        new_node = Node(key, value)
        self.map[key] = new_node
        self.insert(new_node)

        if len(self.map) > self.cap:
            lru = self.tail.prev
            del self.map[lru.key]
            self.remove(lru)


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next, node.prev = None, None

    def insert(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None 


# Your LRUCache object will be instantiated and called as such:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)