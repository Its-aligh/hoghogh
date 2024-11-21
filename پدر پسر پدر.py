class Employee:
    def __init__(self, national_code, firstname, lastname, phone_number, is_marriage, base_salary):
        self.national_code = self.validate_national_code(national_code)
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = self.validate_phone_number(phone_number)
        self.is_marriage = is_marriage
        self.base_salary = base_salary

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
     
    def validate_national_code(self, national_code):
        # validation logic here
        return national_code

    def validate_phone_number(self, phone_number):
        # validation logic here
        return phone_number

    def calculate_salary(self, number_of_days, overtime):
        raise NotImplementedError("This method should be overridden in subclasses")

    def describe_role(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def __str__(self):
        return f"Employee: {self.fullname}, Phone: {self.phone_number}"

class SimpleEmployee(Employee):
    employee_rate = 1.0

    def calculate_salary(self, number_of_days, overtime):
        family_salary = 100  # Assumption for family salary
        working_hours = number_of_days * 8
        return number_of_days * working_hours * self.base_salary + self.is_marriage * family_salary + overtime * self.base_salary * self.employee_rate

    def describe_role(self):
        return "This employee performs simple tasks."

class ServiceEmployee(Employee):
    employee_rate = 1.2

    def calculate_salary(self, number_of_days, overtime):
        family_salary = 150  # Assumption for family salary
        working_hours = number_of_days * 8
        return number_of_days * working_hours * self.base_salary + self.is_marriage * family_salary + overtime * self.base_salary * self.employee_rate

    def describe_role(self):
        return "This employee provides services."

class ManagerEmployee(Employee):
    employee_rate = 1.5

    def calculate_salary(self, number_of_days, overtime):
        family_salary = 200  # Assumption for family salary
        working_hours = number_of_days * 8
        return number_of_days * working_hours * self.base_salary + self.is_marriage * family_salary + overtime * self.base_salary * self.employee_rate

    def describe_role(self):
        return "This employee manages teams and projects."

class CEOEmployee(Employee):
    employee_rate = 2.0

    def calculate_salary(self, number_of_days, overtime):
        family_salary = 300  # Assumption for family salary
        working_hours = number_of_days * 8
        return number_of_days * working_hours * self.base_salary + self.is_marriage * family_salary + overtime * self.base_salary * self.employee_rate

    def describe_role(self):
        return "This employee is the CEO and oversees the entire company."

    def __str__(self):
        return f"CEO: {self.fullname}, Phone: {self.phone_number}"

# Example Usage
employee = SimpleEmployee("1234567890", "John", "Doe", "0123456789", True, 50)
print(employee.calculate_salary(20, 5))
print(employee.describe_role())
