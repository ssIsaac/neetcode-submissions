class PrefixTree:

    class Node:
        def __init__(self,next=None, isEnd=False):
            self.next = {}
            self.isEnd = isEnd
        

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            ## new node
            if w not in curr.next:
                curr.next[w] = self.Node() 
            curr = curr.next[w]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.next:
                return False
            curr = curr.next[w]
            
        return curr.isEnd

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.next:
                return False
            curr = curr.next[w]      
        return True
        
        