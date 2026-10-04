# \n — move to the next line mid-string
print("Line 1\nLine 2\nLine 3")

# \t — align text in columns using tab spacing
print("Name\tScore\tGrade")
print("Alice\t95\tA+")

# \" and \' — quotes inside strings
print("She said, \"Python is amazing!\"")
print('It\'s a beautiful day.')

# \\ — a literal backslash character
print("Path: C:\\Users\\Python")   # → Path: C:\Users\Python

# \u and \N{} — Unicode by code point or name
print("Heart: \u2764 Star: \u2605 Check: \u2713")
print("\N{SNOWMAN} \N{SUN WITH FACE}")   # → ☃ 🌞

# \x — hex escape: H=\x48, e=\x65, l=\x6C, o=\x6F
print("\x48\x65\x6C\x6C\x6F")   # → Hello

# PATHS: escape every backslash manually
path = "C:\\new\\folder"
print(path)   # → C:\new\folder (correct)

# raw format: raw string prefix — cleaner and preferred
path1 = r"C:\new\folder"
print(path1)   # → C:\new\folder (correct and much easier to write)


# Unicode escape — characters specified by code point number
print("\u03C0")                   # → π
print("\u0041\u0042\u0043")       # → ABC
print("\U0001F600")               # → 😀

