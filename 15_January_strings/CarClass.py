class Car:
    def __init__(self, brand, model , year):
        self.brand = brand 
        self.model = model 
        self.year = year 

    def display_info(self):
        print("brand :  ",self.brand) 
        print("model :  ",self.model )
        print("year :  ",self.year)

car1 = Car("Toyota", "Corolla", 2021)  
car2 = Car("Honda", "Civic", 2020)    


car1.display_info()  
car2.display_info() 