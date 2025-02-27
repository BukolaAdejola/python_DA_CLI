'''
data1 = {
    'Name': "ADAMS",
    'ID': 'E7876',
    'SALARY': 50000,
    'DEPARTMENT': 'ACCOUNTING'
}
data2 = {
    'Name': "JONES",
    'ID': 'E7499',
    'SALARY': 45000,
    'DEPARTMENT': 'RESEARCH'
}
data3 = {
    'Name': "MARTIN",
    'ID': 'E7900',
    'SALARY': 50000,
    'DEPARTMENT': 'SALES'
}
data4 = {
    'Name': "SMITH",
    'ID': 'E7698',
    'SALARY': 55000,
    'DEPARTMENT': 'OPERATIONS'
}

Task1: 
Use "assign_department" method to change the department of an employee

Task2: to calculate overtime salary
Use "calculate_emp_salary" method takes two arguments: salary and hours_worked,
which is the number of hour worked by the employee.
If the number of hours worked is more than 50, the method computes overtime
and adds it to the salary.
Overtime is calculated using the following formula:

overtime = hours_worked - 50
overtime_amount = overtime * (salary/50)



'''


class Staff():
    def __init__(self, salary, ID, Name, Department):
        self.salary = salary
        self.ID = ID
        self.Name = Name
        self.Department = Department

    def assign_department(self, newDepartment):
        self.Department = newDepartment
        return (self.Department)
        
    def calculate_emp_salary(self, hours_worked):

        overtime = hours_worked - 50
        overtime_amount = overtime * (self.salary/50)

        print(f'The overtime amount is - {overtime_amount}')
        return f'Total income for the month = {self.salary + overtime_amount}'
    

Staff1 = Staff(
Name = "SMITH",
ID = 'E7698',
salary = 55000,
Department = 'OPERATIONS'
 )

print(Staff1.Department)
print(Staff1.Name)
staff_department = Staff1.assign_department("Marketing")

print(Staff1.Department)
print(Staff1.calculate_emp_salary(72))

