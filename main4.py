print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord("@"))

print(chr(65))
print(chr(97))

ask = input("Enter the character.")

if type(ask) is str and len(ask) == 1:
    print("Value is correct")
else:
    print("Value is wrong. Please try again.")

ascii_val = ord(ask)

print(f"Character: {ask}")
print(f"ASCII Value:{ascii_val}")

if ascii_val >= 65 and ascii_val <= 122:
    print("Type: Uppercase Letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print("Type: Lowercase Letter")
elif ascii_val >= 48 and ascii_val <= 57:
    print("Type: Digit")
elif ascii_val == 32:
    print("Type : Space")
else:
    print("Type: Special Character")
