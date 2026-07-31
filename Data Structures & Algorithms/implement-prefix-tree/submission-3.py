class PrefixTree:

    class Node:
        def __init__(self,val=0,next=None, isEnd=False):
            self.val = val
            self.next = {}
            self.isEnd = isEnd
        

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            w = word[i]
            ## new node
            if w not in curr.next:
                curr.next[w] = self.Node(w) 
            if(i == len(word)-1):
                curr.next[w].isEnd = True
                
            curr = curr.next[w]
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            w = word[i]
            if w in curr.next:
                curr = curr.next[w]
            else:
                return False
            
        print(curr.val)
        if curr.isEnd:
            return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w in curr.next:
                curr = curr.next[w]
            else:
                return False
        return True
        
        