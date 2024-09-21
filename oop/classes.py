class Car:  
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def getName(self):
        print(self.name)

first_car=Car('Tata','safari',2004)
first_car.getName()
