# ====== Superhero and Villain Classes ======
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.__power = power      # private attribute
        self.city = city

    def show_info(self):
        print(f"\nSuperhero: {self.name}")
        print(f"City: {self.city}")
        print(f"Power: {self.__power}")

    def use_power(self):
        print(f"{self.name} uses {self.__power}!")

class Villain(Superhero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.evil_plan = evil_plan

    def show_info(self):
        super().show_info()
        print(f"Evil Plan: {self.evil_plan}")

# ====== Vehicles with Polymorphism ======
class Vehicle:
    def move(self):
        pass  # Generic method

class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")

# ====== Interactive Program ======
def main():
    print("=== Superhero & Villain Creator ===")
    choice = input("Do you want to create a Superhero or Villain? (hero/villain): ").lower()

    name = input("Enter name: ")
    power = input("Enter power: ")
    city = input("Enter city: ")

    if choice == "villain":
        evil_plan = input("Enter evil plan: ")
        character = Villain(name, power, city, evil_plan)
    else:
        character = Superhero(name, power, city)

    character.show_info()
    character.use_power()

    print("\n=== Vehicle Movement Simulator ===")
    vehicles = [Car(), Plane(), Boat()]

    print("Available vehicles: Car, Plane, Boat")
    for v in vehicles:
        print("- ", v.__class__.__name__)
    
    print("\nSimulating movement for all vehicles:")
    for v in vehicles:
        v.move()  # Polymorphic behavior

# Run the program
if __name__ == "__main__":
    main()
