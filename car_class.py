"""
This script defines a simple Car class with the following functionality:
- Stores make, model, and year of a car
- Returns a car's description
- Determines whether the car is considered a classic (25 years or older)

For demonstration, it creates a `Car` object and prints its details and classic status.
"""

class Car:
    def __init__(self, make, model, year):
        """
        Initialize a new Car object.

        Args:
            make (str): Manufacturer of the car (e.g., 'Toyota')
            model (str): Model name (e.g., 'Corolla')
            year (int): Year of manufacture
        """
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        """
        Return the car's description as a tuple.

        Returns:
            tuple: (make, model, year)
        """
        return (self.make, self.model, self.year)

    def is_classic(self):
        """
        Determine if the car is a classic (25 years or older).

        Returns:
            bool: True if the car is classic, False otherwise
        """
        current_year = 1994  # You can update this dynamically using datetime if needed
        return (current_year - self.year) >= 25

# Example usage
car1 = Car("Toyota", "Corolla", 1995)

# Print the car's description
print(car1.get_description())

# Check and print whether the car is a classic
print(car1.is_classic())
