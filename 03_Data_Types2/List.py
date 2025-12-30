#IN python List treatment is same as array
students=["John", "Bob", "Diana"]

students.append("Mani")
print(f"Students are {students}")
#it appends at the end of the list

students.remove("Bob")
print(f"Students after removing Bob: {students}")
#it removes the first occurrence of the value

new_studends=["Eve", "Frank"]
students.extend(new_studends)
#it adds multiple values at the end of the list

print(f"Students after extending the list: {students}") 

last_student=students.pop()
print(f"Removed student: {last_student}")
#it removes and returns the last item in the list
print(f"Students after popping the last student: {students}")

students.reverse()
print(f"Students : {students}")

students.sort()
print(f"Students : {students}")

Suger_levels=[5.6, 4.3, 6.1, 3.9]
print(f"max sugar level is {max(Suger_levels)}")

Suger_levels.insert(2, 4.8 )
print(f"Suger levels after insertion: {Suger_levels}")