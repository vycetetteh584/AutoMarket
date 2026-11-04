import json
class Car:
    def __init__(self, make,model, year, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def to_dict(self):
        return {
            "make": self.make, "model": self.model, "year": self.year, "price": self.price, "mileage" : self.mileage
        }

def save_cars(cars):
    car_data = []

    for car in cars:
        car_data.append(car.to_dict())
    with open("cars.json", "w") as file:
        json.dump(car_data,file)

def load_cars():
    try:
        with open("cars.json", "r",) as file: 
         car_data = json.load(file)
    except FileNotFoundError:
       return []

    cars = []
    for car in car_data:
        new_car = Car(car["make"], car["model"], car['year'], car["price"], car["mileage"])
        cars.append(new_car)
    return cars


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

def car_search(make, max_price, mileage):
    
    found = False
    
    result_list = []
        
    for car in cars:
        make_matches = make== "" or make == car.make.lower()
        price_matches = max_price == "" or max_price >= car.price
        mileage_matches = mileage == "" or mileage >= car.mileage
        
        if (make_matches) and (price_matches) and (mileage_matches):
             result = (car.make, car.model, car.year, car.price, car.mileage)
             result_list.append(result)
             found = True

    if found == False:
        print("No results")
    return result_list

def sort_cars(result_list):
    sorting = input("Sort by price or mileage? ").lower()

    if sorting == "mileage" or sorting == "m":
        index = 4
    elif sorting == "price" or sorting == "p":
        index = 3
    elif sorting == "no":
         return result_list
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

cars = load_cars()

#results = car_search()

while True:
     print("Press 1 to search for cars")
     print("Press 2 to view all cars")
     print("Press 3 to add a car")
     print("E for exit")

     choice = input("Enter your choice: ").lower()

     if choice == "1":
        make = input("Enter manufacturer: ").lower()
        max_price = input("Enter maximum price: ")
        if max_price != "":
            try:
                max_price = int(max_price)
            except ValueError:
                print("Enter a valid number")
                continue
        mileage = input("Enter maximum mileage: ")
        if mileage != "":
            try:
                mileage = int(mileage)
            except ValueError:
                print("Enter a valid number")
                continue
        results =car_search(make, max_price, mileage)
        if results is not None:
            for car in results:
                print(f"{car[0]} {car[1]} | Year: {car[2]} | Price: ${car[3]} | Mileage: {car[4]}")
     elif choice== "2":
          for car in cars:
            print(f"Make: {car.make} {car.model} | Year: {car.year} | Price: ${car.price} | Mileage: {car.mileage}")
     elif choice == "3":
         while True:
            new_make = input("Enter manufacturer: ")
            if new_make.strip() == "":
                print("Manufacturer cannot be empty")
                continue
            break
         while True:
            new_model = input("Enter model: ")
            if new_model.strip() == "":
                    print("Model cannot be empty")
                    continue
            break
         while True:
            new_year = input("Enter year: ")
            if new_year == "":
                print("Year cannot be empty")
                continue
            try:
                new_year = int(new_year)
                if new_year < 1900 or new_year > 2027:
                    print("Must be a year between 1900 and 2027")
                    continue
                break
            except ValueError:
                print("Enter a valid year")
                continue
         while True:
            new_price = input("Enter price: ")
            if new_price == "":
                print("Price cannot be empty")
                continue
            try:
                new_price = int(new_price)
                if new_price < 0:
                    print("Price must be greater than 0")
                    continue
                break
            except ValueError:
                print("Enter a valid price")
                continue
         while True:
            new_mileage = input("Enter mileage: ")
            if new_mileage == "":
                print("Mileage cannot be empty")
                continue
            try:
                new_mileage = int(new_mileage)
                if new_mileage <= 0:
                    print("Mileage cannot be negative")
                    continue
                break
            except ValueError:
                print("Enter a valid mileage")
                continue
         new_car = Car(new_make,new_model,new_year,new_price,new_mileage)
         cars.append(new_car)
         save_cars(cars)
         
     elif choice == "e":
          break
     else:
          print("Invalid choice")
     

#if results is not None:
 #   sorted_results = sort_cars(results)
  #  for car in sorted_results:
   #     print(f"{car[0]} {car[1]} | Year: {car[2]} | Price: ${car[3]} | Mileage: {car[4]}")

