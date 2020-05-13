class Fruit:
    '''this class will be show name and nutrients and sip'''
    def __init__(self,name,nutrients):
        try:
            assert type(nutrients) == list
        except AssertionError:
            print("invalid error")
            raise exception
        self.name = name
        self.nutrients = nutrients
        self.is_rip = False
    
    def get_name(self):
        return self.name
    
    def get_nutrient(self):
        print(self.name+"the nutrishion are follow")
        for value in get_nutrient:
            print(value)
        
    def check_rip(self):
        return self.is_rip
    
    def rip_fruit(self):
        self.is_rip = True

    def __repr__(self):
        return f"{self.name}: {', '.join(self.nutrients)}"



apple = Fruit(name = "apple" , nutrients = ["vA","VB","VC"])

print(apple)