# rstrip():to remove spaces at right hand side
# lstrip():to remove spaces at left hand side
# strip():to remove spaces at both sides

programming = input("Enter your programming language: ")
p_name  = programming.rstrip()
if p_name == "python":
    print(p_name)
elif p_name == "java":
    print(p_name)
elif p_name == "c++":
    print(p_name)
else:
    print("Invalid programming language")