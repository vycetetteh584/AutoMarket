class Car:
    def __init__(self, make,model, year, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
    
def is_affordable(price,budget):
      if budget < price:
            return False
      elif(budget >= price):
            return True
def get_deal_rating(price):
      if price < 22000:
            return "Good Deal"
      elif price >= 22000 and price <= 28000:
            return "Fair Deal"
      else:
            return "Overpriced"

def car_search():
    make = input("Enter manufacturer: ").lower()
    max_price = int(input("Enter maximum price: "))
    mileage = int(input("Enter maximum mileage: ")) 
    found = False


    result_list = []

    for car in cars:
        if (max_price >= car.price) and (make == car.make.lower()) and (mileage >= car.mileage):
            result= (car.make, car.model, car.year, car.price, car.mileage)
            result_list.append(result)
            found = True 

    if found == False:
        print("No results")
    return result_list

def sort_cars(result_list):
    sorting = input("Sort by price or mileage? ").lower()

    if sorting == "mileage":
        index = 4
    elif sorting == "price":
        index = 3
    else:
        print("Invalid sorting option")
        return result_list

    for i in range(len(result_list)):
        for j in range(len(result_list) - 1 - i):
            if result_list[j][index] > result_list[j + 1][index]:
                result_list[j], result_list[j + 1] = result_list[j + 1], result_list[j]

    return result_list
         

car1 = Car("Toyota", "Camry", 2006, 15000, 23000)
car2 = Car("Honda", "Civic", 2015, 23000, 54000)
car3 = Car("BMW", "340i", 2020, 32000, 74300)
car4 = Car("BMW", "540i", 2018, 27000, 78000)

cars = [car1,car2,car3,car4]

results = car_search()
sorted_results = sort_cars(results)

for car in sorted_results:
    print(car)


