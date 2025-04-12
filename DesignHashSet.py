class MyHashSet:
    
    def __init__(self):
        self.ThisSet=set() 
       
        
    def add(self,key):
        self.ThisSet.add(key)
        
    def remove(self, key):
        self.ThisSet.discard(key)
        

    def contains(self, key):
        if key in self.ThisSet:
            return True
        else:
            return False
    
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))