class Employee:
    
    def __init__(self):
        print('Employee created')
        
    def __del__(self):
        print("Destructor called")
        
def cr_obj():
        print('Making object')
        obj=Employee()
        print('function end')
        return obj
    
print('Calling cr_obj() function')
obj=cr_obj()
print('program end')