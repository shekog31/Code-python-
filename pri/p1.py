class myC:
    __pV= 27;
    
    def __pMeth(self):
        print("Inside class")
    def hello(self):
        print("Privat Var value:",myC.__pV)
foo = myC()
foo.hello()
foo.__pMeth
    