a = int(input("Enter any number a : "))
b = int(input("Enter any number b : "))

print(id(a),id(b))
if(a is b):
    print(f"a and b have the same identity")
if(a is not b):
    print(f"a and b do not have the same identity")
