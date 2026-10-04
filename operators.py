#  Arithmetc Operators

# Addition
print(15 + 7) # → 22
# Subtraction
print(15 - 7) # → 8
# Multiplication
print(15 * 7) # → 105
# Division always gives float in Python 3
print(7 / 2) # → 3.5 (float)
print(4 / 2) # → 2.0 (float, not just 2)
# Floor division — rounds DOWN always
print(17 // 5) # → 3 (not 3.4)
print(-17 // 5) # → -4 (rounds DOWN, not towards zero!)
# Modulus — the remainder after floor division
print(17 % 5) # → 2 (17 = 3×5 + 2)
print(10 % 2) # → 0 (10 divides evenly — no remainder)
print(7 % 2) # → 1 (7 is odd)
# Exponentiation
print(2 ** 10) # → 1024
print(64 ** 0.5) # → 8.0 (square root)
#The exponentiation operator ** raises the left operand to the power of the right.
print(27 ** (1/3)) # → 3.0 (cube root)

#  Relational Operators

# Equal to - checks if values are equal
print(10 == 10) # → True
# Not Equal to - checks if values are different
print(10 != 5) # → True
# Greater than - checks if value is greater than
print(10 > 20) # → False
# Less than - checks if value is less than
print(10 < 20)
# Greater than or Equal to - checks if value is greater than or equals to
print(10 <= 10)
# Less than or Equal to - checks if value is less than or equals to
print(10 >= 11)
# Chained comparisons — unique to Python, reads like maths
x = 5
print(1 < x < 10) # → True (x is between 1 and 10)
print(0 <= x <= 5) # → True (x is equal to 5)
print(5 < x < 10) # → False (x is not greater than 5)
# String comparisons — lexicographic (letter by letter)
print("apple" < "banana") # → True ('a' < 'b' in Unicode)
print("Python" == "python") # → False (case-sensitive!)
# Comparing booleans with numbers
print(1 == True) # → True (True equals 1 in Python)
print(0 == False) # → True (False equals 0 in Python)
print(1 == "1") # → False (int and str are different types)


#  Assignment Operators

# Assign — stores a value in a variable
x = 5
print(x)  # → 5
# Add assign — adds to the variable and stores it back (x = x + 3)
x = 10
x += 3
print(x)  # → 13
# Subtract assign — subtracts and stores back (x = x - 2)
x = 10
x -= 2
print(x)  # → 8
# Multiply assign — multiplies and stores back (x = x * 4)
x = 10
x *= 4
print(x)  # → 40
# Divide assign — always gives a float in Python 3
x = 10
x /= 4
print(x)  # → 2.5 (float)
x = 10
x /= 2
print(x)  # → 5.0 (float, not just 5)
# Floor divide assign — rounds DOWN always
x = 17
x //= 5
print(x)  # → 3 (not 3.4)
x = -17
x //= 5
print(x)  # → -4 (rounds DOWN, not towards zero!)
# Modulus assign — stores the remainder after floor division
x = 17
x %= 5
print(x)  # → 2 (17 = 3×5 + 2)
x = 10
x %= 2
print(x)  # → 0 (10 divides evenly — no remainder)
# Power assign — raises the variable to a power and stores back
x = 2
x **= 10
print(x)  # → 1024
x = 64
x **= 0.5
print(x)  # → 8.0 (square root)
# The ** operator raises the left operand to the power of the right.
x = 27
x **= (1/3)
print(x)  # → 3.0 (cube root)



#  Logical Operators

# and — both conditions must be True
age = 20
has_id = True
print(age >= 18 and has_id) # → True (both conditions satisfied)
# or — at least one condition must be True
is_student = True
is_teacher = False
print(is_student or is_teacher) # → True (one is True)
# not — inverts the boolean value
print(not True) # → False
print(not False) # → True
# Short-circuit with 'and' — right side skipped if left is False
print(False and 1/0) # → False (no ZeroDivisionError!)
# Short-circuit with 'or' — right side skipped if left is True
print(True or 1/0) # → True (no ZeroDivisionError!)
# Combining logical operators with comparison operators
marks = 72
print(marks >= 40 and marks <= 100) # → True (valid score range)
print(marks < 40 or marks > 100) # → False (not out of range)



#  Bitwise Operators

# bin() shows the binary representation of any number
print(bin(5)) # → 0b101
print(bin(3)) # → 0b11
# AND — 1 only where both bits are 1
print(5 & 3) # → 1 (0101 & 0011 = 0001)
# OR — 1 where either bit is 1
print(5 | 3) # → 7 (0101 | 0011 = 0111)
# XOR — 1 where bits are different
print(5 ^ 3) # → 6 (0101 ^ 0011 = 0110)
# Left shift — multiply by powers of 2
print(5 << 1) # → 10 (5 × 2)
print(5 << 2) # → 20 (5 × 4)
# Right shift — divide by powers of 2
print(20 >> 1) # → 10 (20 ÷ 2)
print(20 >> 2) # → 5 (20 ÷ 4)


#  Membership Operators
# Membership — checking if a value exists in a sequence
print("py" in "python") # → True
print("Java" in "python") # → False
print("z" not in "hello") # → True


#  Identity Operators

a = [1,2,3]
b = [1,2,3]
c = a
# Identity — == checks value equality, is checks object identity
print(a is b)
print(a is c)
print (a is not b)
print (a is not c)
# id() returns the unique identity of an object (its memory address in CPython)
print(id(a))
print(id(b))
print(id(c))