class parr:
    
    sp="bird"
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
blu=parr("Blue",10)
woo=parr("Woo",15)

print("Blu is a {}".format(blu.sp))
print("Woo is a {}".format(woo.sp))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))