class Car:
    def __init__(self, make,model, year, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

car1 = Car("Toyota", "Camry", 2006, 15000, 23000)
car2 = Car("Honda", "Civic", 2015, 23000, 54000)
car3 = Car("BMW", "340i", 2020, 32000, 74300)
car4 = Car("BMW", "540i", 2018, 27000, 78000)

cars = [car1,car2,car3,car4]
make = input("Enter manufacturer: ").lower()
max_price = int(input("Enter maximum price: "))
mileage = int(input("Enter maximum mileage: "))

found = False

for car in cars:
    rating = ""
    if(car.price < 22000):
            rating = ("Good Deal")
    elif(car.price >=22000 and car.price<=28000):
            rating = ("Fair Deal")
    else:
            rating = ("Overpriced")
    
    if (max_price >= car.price) and (make == car.make.lower()) and (mileage >= car.mileage):
            print(car.make, car.model, car.year, car.price, car.mileage, rating)
            found = True 
if found == False:
    print("No results")
    

