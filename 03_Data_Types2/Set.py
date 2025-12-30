essential={"mani","sunil","rahul"}
optional={"deepak","vikas","rahul"}

all= essential|optional
print("All Students: ",all)
# All Students:  {'mani', 'deepak', 'vikas', 'rahul', 'sunil'}


common=essential&optional
print("common students are: ",common)
# common students are:  {'rahul'}

only_essential= essential - optional
print("only essential students are: ",only_essential)
# only essential students are:  {'mani', 'sunil'}

only_optional= optional - essential
print("only optional students are: ",only_optional)
# only optional students are:  {'vikas', 'deepak'}

print("Is 'mani' in optional set?","mani" in optional)
# Is 'mani' in optional set? False

print("Is 'vikas' in optional set?","vikas" in optional)
# Is 'vikas' in optional set? True
