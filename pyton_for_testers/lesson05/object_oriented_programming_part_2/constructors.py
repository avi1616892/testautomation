#constructors

class Employee:
    employee_count=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count+=1

    def display_count(self):
        print("Total number of employees:" ,Employee.employee_count)

    def display_employee(self):
        print("Name:" , self.name ,"Salary:" , self.salary)

emp1=Employee("Avi",30000)
emp1.display_employee()
emp1.display_count()
emp2=Employee("David",15000)
emp2.display_employee()
emp2.display_count()
