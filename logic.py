"""Operations and Control Flow
File: logic.py
Ask the user to input hours worked.
Use if/elif/else to classify:
Underworked (<20 hours)
Normal (20–40 hours)
Overtime (>40 hours)

Use a for loop to print all employee names.

Use a while loop to repeatedly ask for a task until the user types ""done"".

#telling a person either he/she underworked normal or overworked based on no of working hours
hours_worked=int(input("Enter the no of hours worked: "))
if hours_worked<20:
    print("Underworked")
elif hours_worked<40:
    print("Normal")
else:
    print("Overtime")




 
#list_names=list(input().split(" "))  #not strip()
list_names=["sam", "sanjeev", "sharu", "sankeerth", "sai", "ram", "krishna"]
for word in list_names:
    print(word)"""


   
task=""
while task != "done":
    task=input("Enter a task or type done if finished all tasks: ")

