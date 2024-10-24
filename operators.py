#Arithmetic Operators

a=10
b=20

print(f"Addition operator {a+b}")
print(f"Subtraction operator {b-a}")
print(f"Multiplication operator {a*b}")
print(f"Division operator {a/b}")
print(f"Remainder(modulus) operator {a%b}")
print(f"Exponent operator {a**b}")
print(f"Floor operator {a//b}")


#Comparison Operators
c=57
d=34

print(f"{c} is equal to {d}: {c==d}")
print(f"{c} is not equal to {d}: {c!=d}")
print(f"{c} is greater than  {d}: {c > d}")
print(f"{c} is less than  {d}: {c < d}")
print(f"{c} is greater than or equals to   {d}: {c >= d}")
print(f"{c} is less than or equals to   {d}: {c <= d}")

#Logical Operators
num=10

print(f"is this statement true or false: {num>8 and num<10}")
print(f"is this statement true or false: {num>8 or num<10}")

#Bitwise Operators
e = 10
f = 4

# Print bitwise AND operation
print("e & f =", e & f)

g = 10
h = 4

# Print bitwise OR operation
print("g | h =", g | h)

i = 10
j = 4

# Print bitwise NOT operation
print("~i =", ~i)


#Assignment Operators

# assign 5 to x
x = 5

#Membership Operators
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

