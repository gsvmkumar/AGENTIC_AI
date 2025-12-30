a="mani kumar"
b="Sai Sunil"

print(f"{b} is cleverer than {a}  ")
print(f" first word in first name is: {a[0:10:2]}  ")
# first word in first name is: mn ua

print(f" first word in first name is: {a[5:]}  ")
# first word in first name is: kumar

print(f" first word in first name is: {a[::-1]}  ")
# first word in first name is: ramuk inam 

label_text="Hello welcome to python programming"
encoded_label = label_text.encode("utf-8")
print(f"encoded label is : {encoded_label} ")
decoded_labe= encoded_label.decode("utf-8")
print(f"decoded label is : {decoded_labe} ")