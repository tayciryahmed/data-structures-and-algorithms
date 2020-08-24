import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:
            self.map[val] = len(self.data)
            self.data.append(val)
            return True 
                
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            n = self.map[val]
            
            self.data[n] = self.data[-1]
            self.map[self.data[-1]] = n
            
            self.data.pop()
            del self.map[val]
            
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        n = random.randint(0, len(self.data)-1)
        return self.data[n]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
