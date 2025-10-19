class rec():
    def __init__(self, l ,w):
        self.length = l
        self.width = w
        
    def r_a(self):
        return self.length*self.width
    
nR= rec(12,10)
print(nR.r_a())