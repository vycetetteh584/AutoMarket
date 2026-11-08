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

def car_search(make,model, max_price, mileage, year):
    
    found = False
    
    result_list = []
        
    for car in cars:
        make_matches = make== "" or make == car.make.lower()
        price_matches = max_price == "" or max_price >= car.price
        mileage_matches = mileage == "" or mileage >= car.mileage
        model_matches = model == "" or model == car.model.lower()
        year_matches = year == "" or year == car.year
        
        if (make_matches) and (price_matches) and (mileage_matches) and (model_matches) and (year_matches):
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

def get_valid_text(prompt):
    while True:
        value = input(prompt)

        if value.strip() == "":
            print("Field cannot be empty")
            continue
        return value

def get_valid_number(prompt, min_value, max_value):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Field cannot be empty")
            continue

        try:
            value = int(value)
            if value < min_value or value >max_value:
                print("Number is outside the allowed range")
                continue
            return value
        except ValueError:
            print("Enter a valid number")
            continue        

car1 = Car("Toyota", "Camry", 2006, 15000, 23000)
car2 = Car("Honda", "Civic", 2015, 23000, 54000)
car3 = Car("BMW", "340i", 2020, 32000, 74300)
car4 = Car("BMW", "540i", 2018, 27000, 78000)

cars = load_cars()
fields = ["Make", "Model", "Year", "Price", "Mileage", "Entire Listing"]


#results = car_search()

while True:
     print("Press 1 to search for cars")
     print("Press 2 to view all cars")
     print("Press 3 to add a car")
     print("Press 4 to delete a car")
     print("Press 5 to update a car listing")
     print("E for exit")

     choice = input("Enter your choice: ").lower()

     if choice == "1":
        make = input("Enter manufacturer: ").lower()
        model = input("Enter model: ").lower()
        max_price = input("Enter maximum price: ")
        if max_price.strip() != "":
            try:
                max_price = int(max_price)
            except ValueError:
                print("Enter a valid number")
                continue
        mileage = input("Enter maximum mileage: ")
        if mileage.strip() != "":
            try:
                mileage = int(mileage)
            except ValueError:
                print("Enter a valid number")
                continue
        
        year = input("Enter year: ")
        if year.strip() != "":
            try:
                year = int(year)
            except ValueError:
                print("Emter a valid number")
                continue
        results =car_search(make, model ,max_price, mileage, year)
        if results is not None:
            for car in results:
                print(f"{car[0]} {car[1]} | Year: {car[2]} | Price: ${car[3]} | Mileage: {car[4]}")
     elif choice== "2":
          for index,car in enumerate(cars, start =1):
            print(f" {index}. {car.make} {car.model} | Year: {car.year} | Price: ${car.price} | Mileage: {car.mileage}")
     elif choice == "3":
        new_make = get_valid_text("Enter manufacturer: ")
        new_model = get_valid_text("Enter model: ")
        new_year = get_valid_number("Enter year: ", 1900, 2027)
        new_price = get_valid_number("Enter price: ", 0, 1000000)
        new_mileage = get_valid_number("Enter mileage: ",0, 500000)

        new_car = Car(new_make,new_model,new_year,new_price,new_mileage)
        cars.append(new_car)
        save_cars(cars)
        print("Vehicle added successfully!")
     elif choice == "4":
        if cars == []:
            print("No cars to delete")
            continue
        for index,car in enumerate(cars, start =1):
            print(f" {index}. {car.make} {car.model} | Year: {car.year} | Price: ${car.price} | Mileage: {car.mileage}")
            
  
        delete_car = get_valid_number("Enter the vehicle that you want to delete: ", 1, len(cars))   
        cars.pop(delete_car-1)
        save_cars(cars)
        print("Vehicle deleted successfully!")

     elif choice == "5":
        if cars == []:
            print("No vehicles to update")
            continue
        for index,car in enumerate(cars, start =1):
            print(f" {index}. {car.make} {car.model} | Year: {car.year} | Price: ${car.price} | Mileage: {car.mileage}")
        update_car = get_valid_number("Enter the vehicle that you want to update: ", 1, len(cars))
            
        selected_car = cars[update_car-1]
        for index, field in enumerate(fields, start =1):
            print(f"{index}. {field}")
        update_input = get_valid_number("What would you like to update?: ", 1, 6)
            

        if update_input == 1:
            new_make = get_valid_text("Enter a new manufacturer: ")
            selected_car.make = new_make
            save_cars(cars)
            print("Manufactuter updated successfully")
            
        if update_input == 2:
            new_model = get_valid_text("Enter a new model: ")
            selected_car.model = new_model
            save_cars(cars)
            print("Model updated successfully")
            
            
        if update_input == 3:
            new_year = get_valid_number("Enter a new year: ", 1900, 2027) 
            selected_car.year = new_year
            save_cars(cars)
            print("Year updated successfully")
                                
            
        if update_input == 4:
            new_price = get_valid_number("Enter a new price: ", 0, 1000000)    
            selected_car.price = new_price
            save_cars(cars)
            print("Price updated successfully")

        if update_input == 5:
            new_mileage = get_valid_number("Enter a new mileage: ", 0, 500000)
            selected_car.mileage = new_mileage
            save_cars(cars)
            print("Mileage updated successfully")

        if update_input == 6:
            new_make = get_valid_text("Enter manufacturer: ")
            new_model = get_valid_text("Enter model: ")
            new_year = get_valid_number("Enter year: ", 1900, 2027)
            new_price = get_valid_number("Enter price: ", 0, 1000000)
            new_mileage = get_valid_number("Enter mileage: ", 0, 500000)
               
            selected_car.make = new_make
            selected_car.model = new_model
            selected_car.year = new_year
            selected_car.price = new_price
            selected_car.mileage = new_mileage
            
            save_cars(cars)
            print("Vehicle listing updated successfully")

         
     elif choice == "e":
          break
     else:
          print("Invalid choice")
     

#if results is not None:
 #   sorted_results = sort_cars(results)
  #  for car in sorted_results:
   #     print(f"{car[0]} {car[1]} | Year: {car[2]} | Price: ${car[3]} | Mileage: {car[4]}")

