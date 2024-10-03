class Person:
    def __init__(self, names):
        self.names = names
        self.all_names = []

    def append_names(self):
        for name in self.names:
            self.all_names.append(name)
        return self.all_names

# Example usage
names = ['Kris', 'Anna', 'Eric', 'Neela']
person = Person(names)
appended_names = person.append_names()
print(appended_names)
