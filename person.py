class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, gender={self.gender})"

    def is_older_than(self, other_person):
        if not isinstance(other_person, Person):
            raise ValueError("Argument must be of type Person")
        return self.age > other_person.age

# Create instances of the Person class
person1 = Person(name="Kelvin K", age=23, gender="Male")
person2 = Person(name="Scola K", age=22, gender="Female")

# Call the introduce method
person1.introduce()
person2.introduce()

# Print string representation
print(person1)
print(person2)

# Compare ages
print(f"Is {person1.name} older than {person2.name}? {'Yes' if person1.is_older_than(person2) else 'No'}")
