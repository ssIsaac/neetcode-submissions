class Node:
    def __init__(self, key, value):
        self.key, self.value = key,value
        self.prev = self.next = None, None



class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
        self.cache = {}

    ## add to right
    def insert(self,node):
        tmp = self.right.prev
        tmp.next = self.right.prev = node 
        node.next = self.right
        node.prev = tmp


    
    ## remove any node
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if(key in self.cache):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        while(len(self.cache) > self.cap):
            tmp = self.left.next
            self.remove(tmp)
            self.cache.pop(tmp.key)

            # lru = self.left.next
            # self.remove(lru)

        
