class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self, beverage):
        self.beverage = beverage

    def display_menu(self):
        print("Welcome to the vending machine!")
        for i, drink in enumerate(self.beverage,start=1):
            print(f"{i}. {drink.name} - ${drink.price:2f}")
        print("7.Exit")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                print("Thank you for using The vending machine!")
                break
            if not choice.isdigit() or not (1 <= int(choice) <= 6):
                print("Please enter a valid choice.")
                continue
            drink_index = int(choice) - 1
            beverage = self.beverage[drink_index]
            print(f"You selected: {beverage.name} (${beverage.price:2f})")
            money = float(input("Enter your money: "))

            if money < beverage.price:
                print("Sorry, you don't have enough money. Transaction cancelled.\n")
            else:
                change = money - beverage.price
                print(f" Vending {beverage.name}...")
                print(f" Your change is ${change:2f}\n")

drink1 = Beverage("Coke", 1.50)
drink2 = Beverage("Sprite", 1.50)
drink3 = Beverage("Water", 1.00)
drink4 = Beverage("Gatorade", 2.25)
drink5 = Beverage("Icetea", 1.75)
drink6 = Beverage("Fanta", 1.75)

beverage_list = [drink1, drink2, drink3, drink4, drink5, drink6]

machine = VendingMachine(beverage_list)
machine.start()

