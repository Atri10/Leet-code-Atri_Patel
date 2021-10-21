import random
class RandomizedSet:
    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:return False
        else:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True
            
    def remove(self, val: int) -> bool:
        if val in self.hashmap: 
            last_el = self.arr[-1]
            val_index = self.hashmap[val]
            self.hashmap[last_el] = val_index
            self.arr[val_index] = last_el
            self.arr[-1] = val
            self.arr.pop()
            self.hashmap.pop(val)
            return True
        else:return False
            
    def getRandom(self) -> int:
        return random.choice(self.arr)