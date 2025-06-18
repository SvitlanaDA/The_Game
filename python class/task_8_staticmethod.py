"""Метод класу та статичний метод
Задача:

Створіть клас Employee з наступним:
name (рядок)
salary (з плаваючою точкою)
Додайте класовий метод from_string(), який створює екземпляр Employee з рядка у форматі "name, salary"
Додайте статичний метод is_high_salary(), який перевіряє, чи зарплата працівника перевищує 100,000
Продемонструйте створення працівника з рядка та перевірку його зарплати

Приклад виводу:

Employee name: Alice, Salary: 120000
Is the salary high? True"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def from_string(cls, employee_string):
        """Створює Employee з рядка 'name,salary'."""
        name, salary = employee_string.split(',')
        return cls(name, float(salary))
    
    @staticmethod
    def is_high_salary(salary):
        """Перевіряє, чи зарплата працівника перевищує 100,000."""
        return salary > 100000


# Створення екземплярів
employees = [
    Employee.from_string("Alicea,12000"),
    Employee.from_string("Alice,120000"),
    Employee.from_string("Bob,25000")
]

# Виведення інформації для кожного працівника
for employee in employees:
    print(f"Employee name: {employee.name}, Salary: {employee.salary}")
    print(f"Is the salary high? {Employee.is_high_salary(employee.salary)}")