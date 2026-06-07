text = 'python'
print(text[0])

# methods
s = "aBCDEF"
s = "A" + s[1:]
print(s)
# concept of immutable but creates new string
s3 = "ABCDEF"
s4 = "H" + s[1:]
s5 = s.replace("ABC", "abc")

print(s4)
print(s5)

print(len(s3))
s.upper()
s.lower()

# f string
name = "priya"
print(f"name is, {name}")
