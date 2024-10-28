class Car():
    def __init__(self,make,model,year):
        self.make =make
        self.model =model
        self.year = year

    def get_description(self):
        return (self.make,self.model,self.year)

    def is_classic(self):  
        current_year =1994
        return(current_year-self.year) >= 25
        #if (  current_year-self.year) >= 25:
        #    return True

car1 =Car("Toyota","COrolla",1995)
print(car1.get_description())
print(car1.is_classic())