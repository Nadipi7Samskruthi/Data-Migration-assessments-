"""
2.1 List of Employees
Create a list of employee dictionaries.
Add a new employee to the list.
Remove an employee from the list.
Print the total number of employees."""

employee_list=["Sharadha","Sanjeev","Sankeerth"]
print("All employees names: ",employee_list)
#Add a new employee to the list.
employee_list.append("Chintu")
print("After adding a new employee to the list: ",employee_list)
#Remove an employee from the list.
employee_list.remove("Sanjeev")
print("After removing an employee from the list: ",employee_list)
print("Total number of employees: ",len(employee_list))



print("\n")

"""
2.2 Task Dictionary
Create a dictionary where keys are employee IDs and values are lists of assigned tasks.
Add a task to an employee.
Remove a task from an employee.
Print all tasks for all employees."""


my_dict={
    1:["debugging"],
    2:["coding"],
    3:["testing"]}

print(my_dict)
#Add a task to an employee.
my_dict[1].append("singing")
print("After adding a task to an employee: ",my_dict)
#Remove a task from an employee.
my_dict[2].remove("coding")
print("After removing a task from an employee: ",my_dict)
print("printing all tasks for all employees: ", my_dict.values())




print("\n")


"""
2.3 Unique Skills Using Sets
Create a set containing all unique employee skills.
Add two new skills to the set.
Print the final set of skills."""

my_set={"Python","Databricks","ETL"}
print("printing the set",my_set)
my_set.add("Java")
my_set.add("c")
print("After adding two new skills to the set: ",my_set)
my_set.add("Python")
print("After adding a duplicate skills to the set: ",my_set)




print("\n")

"""
2.4 Company Holidays Using Tuples
Create a tuple of company holiday dates.
Attempt to change an element and if it fails, Write a comment explaining it."""


my_tuple=("1/1/2025","14/1/2025","23/1/2025")
print("Holidays dates of company: ",my_tuple)
#Attempting to change an element of tuple.
my_tuple[1]="2/1/2025"
print(my_tuple)

"""tuple is immutable,so we can't add items in tuple.
If we want to add any items to tuple we should convert then to list,
make changes and covert back to tuple"""









