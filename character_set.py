#Ordinal Function
print(ord('A'))
print(ord('a'))
print(ord('👌'))

#Character Function
print(chr(65))
print(chr(67))
print(chr(69))
print(chr(95))
print(chr(97))

# ASCII code [UniCode]
"""48–57 → digits '0' through '9'  
·  65–90 → uppercase 'A' through 'Z' 
·  97–122 → lowercase 'a' through 'z'."""

# Category 1 — Letters: used in names
studentName = "Priya"

# Category 2 — Digits: numeric literal
marks = 95

# Category 3 — Special symbols: operators and brackets
total = (marks + 5) * 2

# Category 4 — Whitespace: indentation is mandatory in Python
if marks > 90:
    print("Distinction!")   # 4 spaces — mandatory

# Category 6 — Unicode: works natively in Python 3
print(f"नमस्ते {studentName}! Score: {marks} 🎉")

# More Examples

# Direct Unicode characters in strings — works with no setup
print("नमस्ते Python!")            # Nepali
print("π = 3.14159 €50 £30")      # Symbols

# Unicode variable names — unusual but perfectly valid in Python 3
मूल्य = 1500
print(f"मूल्य: {मूल्य}")           # → मूल्य: 1500