class AutomobileDealership:
    def __init__(self):
        self.bikes = {
            "Honda Shine": 10,
            "Yamaha FZ": 8,
            "Suzuki Gixxer": 5,
            "Royal Enfield Classic": 3
        }

    def view_all_bikes(self):
        print("\nAvailable Bikes and Stock:")
        total_quantity = 0
        for bike, stock in self.bikes.items():
            print(f"{bike}: {stock} units")
            total_quantity += stock
        print(f"\nTotal number of bikes in stock: {total_quantity}")

    def purchase_bike(self):
        bike_name = input("\nEnter the name of the bike you want to purchase: ")
        if bike_name in self.bikes:
            if self.bikes[bike_name] > 0:
                self.bikes[bike_name] -= 1
                print(f"\n{bike_name} purchased successfully!")
            else:
                print(f"\nSorry, {bike_name} is out of stock.")
        else:
            print("\nBike model not found.")

    def update_stock(self):
        bike_name = input("\nEnter the name of the bike to update stock: ")
        if bike_name in self.bikes:
            try:
                additional_stock = int(input("Enter the number of units to add: "))
                if additional_stock > 0:
                    self.bikes[bike_name] += additional_stock
                    print(f"\nStock updated! {bike_name} now has {self.bikes[bike_name]} units.")
                else:
                    print("\nPlease enter a positive number.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        else:
            print("\nBike model not found.")

    def delete_bike_model(self):
        bike_name = input("\nEnter the name of the bike model to delete: ")
        if bike_name in self.bikes:
            del self.bikes[bike_name]
            print(f"\n{bike_name} has been removed from the inventory.")
        else:
            print("\nBike model not found.")
    def add_bike_model(self):
        bike_name = input("\nEnter the name of the bike model to Add: ")
        st = int(input("\nEnter the Stock of the bike model that u adding: "))
        self.bikes.update({bike_name:st})

    def menu(self):
        while True:
            print("\nAutomobile Dealership")
            print("1. View All Bikes")
            print("2. Purchase a Bike")
            print("3. Update Stock")
            print("4. Delete Bike Model")
            print("5. Add Bike Model")
            print("6. Exit")
            

            choice = input("\nEnter choice (1-6): ")

            if choice == "1":
                self.view_all_bikes()
            elif choice == "2":
                self.purchase_bike()
            elif choice == "3":
                self.update_stock()
            elif choice == "4":
                self.delete_bike_model()
            elif choice == "5":
                self.add_bike_model()
            elif choice == "6":
                print("\nExiting the system. Thank you!")
                break
            else:
                print("\nInvalid choice. Please try again.")

# Create an instance of the dealership and run the menu
dealership = AutomobileDealership()
dealership.menu()
