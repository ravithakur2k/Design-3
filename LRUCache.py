# Time complexity: O(1) for all the functions since we are using hashmap for retrieving and then remove and add node we are using a doubly linked list
# Space complexity: O(n) at most there there can n elements in the cache based on the capacity
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#Intuition here is to use a hashmap to retrieval so as to save time in getting the value and to maintain the cache order for least recently used we are using a doubly linked list

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.removeNode(self.hashmap[key])
            self.addToHeader(node)
            return node.val
        else:
            return -1

    def removeNode(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        node.next = None
        node.prev = None

    def addToHeader(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            curr = self.hashmap[key]
            curr.val = value
            self.removeNode(curr)
            self.addToHeader(curr)
        else:
            if len(self.hashmap) == self.cap:
                # Remove the LRU node from hashmap and DLL
                nodeToRemove = self.tail.prev
                self.removeNode(nodeToRemove)
                del self.hashmap[nodeToRemove.key]
            new_node = Node(key, value)
            self.hashmap[key] = new_node
            self.addToHeader(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)