class veh:
    
    def __init__(self, name, max_speed, fare):
        self.name = name
        self.max_speed = max_speed
        self.fare = fare
        
class Bus(veh):
    pass

sch_b = Bus("School Volvo", 180, 2500)
print("Vehicle name:", sch_b.name, "Speed", sch_b.max_speed, "Busfare:", sch_b.fare)