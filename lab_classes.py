class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age} years old"


class GoogleEmployee(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}"

    def promote(self, new_salary):
        self.salary = new_salary
        return f"{self.name} has been promoted and now earns {self.salary}"


worker1 = Worker("John", 30)
worker2 = Worker("Alice", 25)
google_employee = GoogleEmployee("Bob", 35, 100000)

print(worker1)
print(google_employee)

print(google_employee.get_details())

new_salary = 120000
print(google_employee.promote(new_salary))
print(google_employee.get_details())
