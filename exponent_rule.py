"""
📝 PYTHON NOTE: EXPONENT ASSOCIATIVITY RULE

In Python, the exponentiation operator (**) evaluates from RIGHT TO LEFT.
This means chained exponents are calculated from the right side first.
"""

# =====================================================================
# 🔹 Example 1: 2 ** 3 ** 2
# =====================================================================

# How Python reads it: 2 ** (3 ** 2)
# Step 1: 3 ** 2 = 9
# Step 2: 2 ** 9 = 512
result_1 = 2 ** 3 ** 2
print(f"Default (Right-to-Left): 2 ** 3 ** 2 = {result_1}")  # Outputs: 512

# To get 64, you must force Left-to-Right with parentheses:
forced_64 = (2 ** 3) ** 2
print(f"Forced (Left-to-Right):  (2 ** 3) ** 2 = {forced_64}")  # Outputs: 64


# =====================================================================
# 🔹 Example 2: 4 ** 3 ** 2
# =====================================================================

# How Python reads it: 4 ** (3 ** 2)
# Step 1: 3 ** 2 = 9
# Step 2: 4 ** 9 = 262144
result_2 = 4 ** 3 ** 2
print(f"Default (Right-to-Left): 4 ** 3 ** 2 = {result_2}")  # Outputs: 262144

# To get a 4-digit result (4,096), force Left-to-Right with parentheses:
forced_4096 = (4 ** 3) ** 2
print(f"Forced (Left-to-Right):  (4 ** 3) ** 2 = {forced_4096}")  # Outputs: 4096


# =====================================================================
# 💡 KEY TAKEAWAY
# =====================================================================
# Without parentheses (), Python ALWAYS solves the exponents at the
# far right side of the chain before moving to the left.

# How Python reads it: 2 ** (2 ** (2 ** 2))
# Step 1 (Far right): 2 ** 2 = 4
# Step 2 (Middle): 2 ** 4 = 16
# Step 3 (Final step): 2 ** 16 = 65536
# Output: 65536
print(2 ** 2 ** 2 ** 2)
