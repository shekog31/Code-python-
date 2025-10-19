class India():
    def capital(self):
        print("New Delhi is thge capital of India")
        
    def language(self):
        print("Hindi is the primary language")
        
    def type(self):
        print("India is a developing country")
        
class USA():
    def capital(self):
        print("Washington is thge capital of India")
        
    def language(self):
        print("English is the primary language")
        
    def type(self):
        print("USA is a developing country")
        
obj_ind=India()
obj_usa=USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()