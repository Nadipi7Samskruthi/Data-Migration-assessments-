"""Assignment-4 Part 4: Functions for Productivity Analysis
File: analytics.py"""


"""#Function: calculate_pay(hours, rate)
#Return total pay.
def calculate_pay(hours, rate):
    return hours * rate
pay = calculate_pay(10, 150)
print("Total Pay:", pay)"""



"""
def calculate_pay(hours, rate):
    return hours * rate
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))
pay = calculate_pay(hours, rate)
print("Total Pay: ", pay)"""


"""
#2.Function: employee_statistics(hours_list)
#Return max, min, and average hours.
def employee_statistics(hours_list):
    return max(hours_list), min(hours_list), sum(hours_list)/len(hours_list)
hours = [8, 4, 3, 6, 8, 11]
maximum, minimum, average = employee_statistics(hours)
print("Max:", maximum)
print("Min:", minimum)
print("Avg:", average)
"""

"""
def employee_statistics(hours_list):
    return max(hours_list), min(hours_list), sum(hours_list)/len(hours_list)
hours = list(map(float, input("Enter hours of employees separated by space: ").split()))
maximum, minimum, average = employee_statistics(hours)
print("Max:", maximum)
print("Min:", minimum)
print("Avg:", average)"""


#3.
#Function: search_employee(employees, emp_id)
#Return employee details if found, otherwise ""Employee not found"".
def search_employee(employees, emp_id):
    for emp in employees:
        if emp['id'] == emp_id:
            return emp
    return "Employee not found"
employees = [
    {"id":101, "name": "Sam", "work":"eating"},
    {"id":102, "name": "Sai", "work":"sleeping"},
    {"id":103, "name":"Ram", "work":"drinking"},
    {"id":104, "name":"Mom", "work":"playing"},
    {"id":105, "name":"Dad", "work": "dancing"}
]
emp_id = int(input("Enter employee ID: "))
print(search_employee(employees, emp_id))





