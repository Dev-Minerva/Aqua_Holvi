


# Parent class
class Employee:
    def emp_info(self, name, age):
        print('Name:', name, 'Age:', age)

# Child class
class Salary(Employee):
    def sal_info(self, basic, hra, da, pf):
        net = basic + hra + da - pf
        print('Employee Salary:', net)

# Create object of the Salary class
emp = Salary()
emp.emp_info('Aqua', 56)
emp.sal_info(25000, 8000, 2400, 579)
