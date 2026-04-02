a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Relational (Comparison) Operators
print("\n Relational Operators ")
print("Equal to :", a == b)
print("Not Equal to", a != b)
print("Greater than:", a > b)
print("Lessthan:", a < b)
print("Greater than or equal to:", a >= b)
print(":Lessthan or equal to:", a <= b)

# Logical Operators
print("\n Logical Operators  ")
print("Logical AND:", (a > 0 and b > 0))
print("Logical OR:", (a > 0 or b > 0))
print("Logical NOT:", not(a > 0))

# Assignment Operators
print("\n Assignment Operators ")
c = a
print("c = a:", c)
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
c/=b
print("c /= b:",c)
c//=b
print("c //= b:",c)
c**=b
print("c ** b:",c)
# Bitwise Operators
print("\n Bitwise Operators ")
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Negation:", ~a)
print("LEFT SHIFT", a << 1)
print("RIGHT SHIFT:", a >> 1)
