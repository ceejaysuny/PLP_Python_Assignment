# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.



# Base class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages - {self.genre}."

    def is_long_book(self):
        return self.pages > 300


# Derived class
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size, format_type):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size  # in MB
        self.format_type = format_type  # e.g., PDF, EPUB, MOBI

    def get_summary(self):
        base_summary = super().get_summary()
        return f"{base_summary} (E-Book: {self.file_size}MB, {self.format_type} format)"

    def is_large_file(self):
        return self.file_size > 50  # File size threshold


# Another derived class
class Audiobook(Book):
    def __init__(self, title, author, pages, genre, duration, narrator):
        super().__init__(title, author, pages, genre)
        self.duration = duration  # in hours
        self.narrator = narrator

    def get_summary(self):
        base_summary = super().get_summary()
        return f"{base_summary} (Audiobook: {self.duration} hours, narrated by {self.narrator})"

    def is_long_audiobook(self):
        return self.duration > 10


# Example usage
if __name__ == "__main__":
    # Create instances
    physical_book = Book("To Kill a Mockingbird", "Harper Lee", 281, "Fiction")
    ebook = EBook("1984", "George Orwell", 328, "Dystopian", 1.2, "EPUB")
    audiobook = Audiobook("Becoming", "Michelle Obama", 426, "Memoir", 19, "Michelle Obama")

    # Call methods
    print(physical_book.get_summary())
    print("Is long book?", physical_book.is_long_book())
    print(ebook.get_summary())
    print("Is large file?", ebook.is_large_file())
    print(audiobook.get_summary())
    print("Is long audiobook?", audiobook.is_long_audiobook())





# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()).
#  However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Polymorphism in action
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Example usage
if __name__ == "__main__":
    # Create a list of vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Demonstrate polymorphism
    print("How do these vehicles move?")
    demonstrate_movement(vehicles)
