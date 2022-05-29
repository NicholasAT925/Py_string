TheString = "Rayla is my Fav Character"

print(TheString)
print(TheString[3], TheString[4])
print("\n")
for i in TheString:
    print(i)
print("\n")
print(TheString[-1], TheString[-2])
s1 = ''
for c in TheString:
    # s1 = s1 + c # this will produce the same string as given string to reverse
    s1 = c + s1 
print(s1)
print(TheString[::-1])
