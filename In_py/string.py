TheString = "Rayla is my Fav Character"

print(TheString)
print(TheString[3], TheString[4]) # print the first 2 characters
print("\n")
for i in TheString: # print the characters of the string
    print(i)
print("\n")
print(TheString[-1], TheString[-2]) # printing the last 2 characters of the string
s1 = '' # emptry variable to hold the new string
for c in TheString:
    # s1 = s1 + c # this will produce the same string as given string to reverse
    s1 = c + s1 

print(s1)
print(TheString[::-1]) # The best and simplest way to reverse a string is by slicing
print("\n")
for c in TheString[-1::-1]: # printing the letters of the string in reverse
    print(c)
print("\n")
Computer_parts = ["Monitor", "mouse", "PC_Tower"]
print(Computer_parts[0][2]) # Output: n