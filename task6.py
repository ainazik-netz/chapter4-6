
class House:
    def __init__(self,household_type,total_area):
        self.household_type = household_type
        self.total_area = total_area
        self.remaining_area = 0
        self.furniture = []
    def add_furniture(self,**kwargs):
        # furniture = []
        self.remaining_area = self.total_area - sum(kwargs.values())
        self.furniture.append(list(kwargs.keys()))
        
    def result(self):                                               
        result_ = 'Type of the house:', self.household_type, 'total area: ', self.total_area
        result_ += 'remaining area: ', self.remaining_area
        result_ += ' number of furniture: ', self.furniture
        return result_
    
       
       
obj = House('brick',18)                       
obj.add_furniture(chair = 1.5, bed = 4, wardrobe = 2)
print(obj.result())




