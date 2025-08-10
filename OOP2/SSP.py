class bir:
    def __init__(self):
        print("Bird is ready")
    def wit(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
        
class pen(bir):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def wit(self):
        print("Penguin")
    def run(self):
        print("Rune faster")
        
peg = pen()
peg.wit()
peg.swim()
peg.run()