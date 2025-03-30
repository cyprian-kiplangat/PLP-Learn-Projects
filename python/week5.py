class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, make, model, year, color):
        """Initialize Vehicle attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._mileage = 0  # Protected attribute
        
    def start_engine(self):
        """Start the vehicle's engine"""
        return f"The {self.color} {self.make} {self.model}'s engine starts."
    
    def move(self):
        """Generic movement method to be overridden by subclasses"""
        return "The vehicle is moving."
    
    def stop(self):
        """Stop the vehicle"""
        return f"The {self.make} {self.model} has stopped."
    
    def get_description(self):
        """Return a description of the vehicle"""
        return f"{self.year} {self.color} {self.make} {self.model}"
    
    def get_mileage(self):
        """Getter for the protected mileage attribute"""
        return self._mileage
    
    def add_trip(self, miles):
        """Add miles to the vehicle's mileage"""
        if miles > 0:
            self._mileage += miles
            return f"Added {miles} miles. New mileage: {self._mileage}"
        return "Miles must be positive."


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, body_type, doors):
        """Initialize Car with Vehicle attributes plus car-specific ones"""
        super().__init__(make, model, year, color)
        self.body_type = body_type
        self.doors = doors
        self.__fuel_level = 100  # Private attribute
    
    def move(self):
        """Override the move method for Car"""
        return f"The {self.make} {self.model} is driving on the road."
    
    def honk(self):
        """Car-specific method"""
        return "Beep! Beep!"
    
    def get_fuel_level(self):
        """Getter for the private fuel_level attribute"""
        return f"Fuel level: {self.__fuel_level}%"
    
    def refuel(self, amount):
        """Add fuel to the car"""
        if 0 < amount <= 100:
            self.__fuel_level = min(100, self.__fuel_level + amount)
            return f"Refueled. New fuel level: {self.__fuel_level}%"
        return "Invalid refuel amount."


class Boat(Vehicle):
    """Boat class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, boat_type, length):
        """Initialize Boat with Vehicle attributes plus boat-specific ones"""
        super().__init__(make, model, year, color)
        self.boat_type = boat_type
        self.length = length
    
    def move(self):
        """Override the move method for Boat"""
        return f"The {self.make} {self.model} is sailing across the water."
    
    def anchor(self):
        """Boat-specific method"""
        return f"The {self.boat_type} boat has dropped its anchor."


class Plane(Vehicle):
    """Plane class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, max_altitude, wingspan):
        """Initialize Plane with Vehicle attributes plus plane-specific ones"""
        super().__init__(make, model, year, color)
        self.max_altitude = max_altitude
        self.wingspan = wingspan
        
    def move(self):
        """Override the move method for Plane"""
        return f"The {self.make} {self.model} is flying through the air at {self.max_altitude} feet."
    
    def takeoff(self):
        """Plane-specific method"""
        return f"The {self.make} {self.model} is taking off."
    
    def land(self):
        """Plane-specific method"""
        return f"The {self.make} {self.model} is landing."


def demonstrate_polymorphism(vehicles):
    """Demonstrate polymorphic behavior with a list of different vehicles"""
    print("\nDemonstrating Polymorphism:")
    for vehicle in vehicles:
        print(f"{vehicle.get_description()} - {vehicle.move()}")


def main():
    """Main function to demonstrate the vehicle classes"""
    # Create different vehicle objects
    sedan = Car("Toyota", "Camry", 2022, "Blue", "Sedan", 4)
    yacht = Boat("Sea Ray", "Sundancer", 2021, "White", "Yacht", 40)
    jet = Plane("Boeing", "747", 2020, "White", 35000, 225)
    
    # Demonstrate inheritance and method overriding
    print("\nVehicle Information:")
    print(f"Car: {sedan.get_description()}")
    print(f"Boat: {yacht.get_description()}")
    print(f"Plane: {jet.get_description()}")
    
    # Demonstrate specific methods
    print("\nVehicle-specific actions:")
    print(f"Car: {sedan.honk()}")
    print(f"Boat: {yacht.anchor()}")
    print(f"Plane: {jet.takeoff()}")
    
    # Demonstrate encapsulation
    print("\nEncapsulation examples:")
    print(f"Initial mileage for {sedan.get_description()}: {sedan.get_mileage()}")
    print(sedan.add_trip(100))
    print(f"Car fuel info: {sedan.get_fuel_level()}")
    print(sedan.refuel(20))
    
    # Demonstrate polymorphism with a list of vehicles
    vehicles = [sedan, yacht, jet]
    demonstrate_polymorphism(vehicles)


if __name__ == "__main__":
    main()