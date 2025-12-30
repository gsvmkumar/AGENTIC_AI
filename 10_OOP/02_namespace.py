class Employee:
    # Company-wide policies (Class Variables)
    company_name = "TechNova Pvt Ltd"
    working_hours = 8
    is_remote_allowed = True


# -------------------------------
# Company policy change
# -------------------------------
Employee.working_hours = 9
print("Company Working Hours:", Employee.working_hours)


# -------------------------------
# Employee 1
# -------------------------------
emp1 = Employee()
emp1.name = "Ravi"
emp1.working_hours = 8     # Personal adjustment
emp1.is_remote_allowed = False

print("\nEmployee 1 Details")
print("Name:", emp1.name)
print("Company:", emp1.company_name)
print("Working Hours:", emp1.working_hours)
print("Remote Allowed:", emp1.is_remote_allowed)


# -------------------------------
# Employee 2
# -------------------------------
emp2 = Employee()
emp2.name = "Anita"

print("\nEmployee 2 Details")
print("Name:", emp2.name)
print("Company:", emp2.company_name)
print("Working Hours:", emp2.working_hours)
print("Remote Allowed:", emp2.is_remote_allowed)
