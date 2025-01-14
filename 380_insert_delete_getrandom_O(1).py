import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.hashmap[val] = self.n
            self.array.append(val)
            self.n += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.array[idx] = endval
            endval = self.array.pop()
            self.hashmap[endval] = idx
            del self.hashmap[val]
            self.n -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        i = random.randint(0, self.n-1)
        return self.array[i]
        

["RandomizedSet","insert","insert","getRandom","getRandom","insert","remove","getRandom","getRandom","insert","remove"]
[[],[3],[3],[],[],[1],[3],[],[],[0],[0]]
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(3))
print(obj.insert(3))
print(obj.getRandom())
print(obj.getRandom())
print(obj.insert(1))
print(obj.remove(3))
print(obj.getRandom())
print(obj.getRandom())
print(obj.insert(0))
print(obj.remove(0))