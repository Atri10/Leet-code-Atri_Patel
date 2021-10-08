class Trie:

    def __init__(self):
        self.mylist = []
        
    def insert(self, word: str) -> None:
        self.mylist.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.mylist:return True
        else:return False
        

    def startsWith(self, prefix: str) -> bool:
        if not self.mylist:return False
        for i in range(len(self.mylist)):
            curworld = self.mylist[i]
            if len(prefix)>len(curworld):continue
            if prefix[0] != curworld[0]:continue
            pl = len(prefix)
            if prefix==curworld[:pl]:return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
