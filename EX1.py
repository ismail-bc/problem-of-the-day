class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_departmen):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_departmen = emp_departmen
    
    def calculate_emp_salary(self,emp_salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            Oerttime_amount = (overtime * (emp_salary / 50))
            emp_salary = emp_salary + Oerttime_amount
            return f"{emp_salary}"
        else:
            return f"{emp_salary}"

            
    def emp_assign_department(self,emp_departmen):
       self.emp_departmen = emp_departmen
       return f"{self.emp_departmen} is {self.emp_name}'s  new departmnet"
    def print_employee_details(self):
       return f"""Employee naem:{self.emp_name}\nEmployee id:{self.emp_id}.\nEmployee salary:{self.emp_salary},
Employee department:{self.emp_departmen}."""

def main():
    a = Employee(1,"ahmed",1000,"enginering")
    print(a.calculate_emp_salary(1000, 51))
main()