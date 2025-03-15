# Base Class
class Vehicle:
    def __init__(self, vt, rp):
        self.vt = vt
        self.rp = rp

    def VA(self, stock, agency):
        print(f"The available {self.vt} are {stock} with rent of Rs {self.rp} per day of {agency} agency")


# Derived Class
class RentalAgencies(Vehicle):
    def __init__(self, agency, vt, rp):
        super().__init__(vt, rp)
        self.agency = agency

    def rental_period(self):
        while True:
            try:
                p = int(input("Enter the rental period (in days): "))
                if p > 0:
                    return p
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


# Derived Class
class RentalTransaction(RentalAgencies):
    def __init__(self, agency, vt, stock, rp):
        super().__init__(agency, vt, rp)
        self.stock = stock

    def calculate_amount(self, period, quantity):
        total = period * self.rp * quantity
        if period > 7:
            discount = 0.1 * total  # 10% discount for rentals longer than a week
            total -= discount
            print(f"A 10% discount has been applied. You saved Rs {discount}.")
        return total


print("                                  Car and Bus Rental System                  ")
print("----------------------------------------------------------------------------------------------------------------")

# Initial Stock
car_stock = 200
car_rent = 25
bus_stock = 100
bus_rent = 50

while True:
    print("\nPlease enter your choice:")
    print("1: Rent a Car\n2: Rent a Bus\n3: View Stock\n4: Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            vehicle = RentalTransaction("Star", "Car", car_stock, car_rent)
            vehicle.VA(car_stock, vehicle.agency)
            quantity = int(input("Enter the number of cars: "))

            if quantity <= 0 or quantity > car_stock:
                print("Invalid quantity.")
                continue

            period = vehicle.rental_period()
            amount = vehicle.calculate_amount(period, quantity)
            car_stock -= quantity
            print(f"Your order for {quantity} Cars from Star agency is booked. Please pay Rs {amount}.")

        elif choice == 2:
            vehicle = RentalTransaction("Royal", "Bus", bus_stock, bus_rent)
            vehicle.VA(bus_stock, vehicle.agency)
            quantity = int(input("Enter the number of buses: "))

            if quantity <= 0 or quantity > bus_stock:
                print("Invalid quantity.")
                continue

            period = vehicle.rental_period()
            amount = vehicle.calculate_amount(period, quantity)
            bus_stock -= quantity
            print(f"Your order for {quantity} Buses from Royal agency is booked. Please pay Rs {amount}.")

        elif choice == 3:
            print(f"Available Cars: {car_stock}, Rent per Car: Rs {car_rent} per day")
            print(f"Available Buses: {bus_stock}, Rent per Bus: Rs {bus_rent} per day")

        elif choice == 4:
            print("Thank you for using the Rental System!")
            break

        else:
            print("Invalid choice. Please select again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")