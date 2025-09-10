# len(12345)
print(len('12345'))

x = 12345
y = 'Test'
z = True
zz = 12.34
print(type(x))
print(type(y))
print(type(z))
print(type(zz))\


# convert int to str
print(type(str(x)))
# convert to int and add
print(int("123") + int("456"))
print(float("123") + float("456"))

# fix type error
print("Number of letters in your name: " +
      str(len(input("Enter your name"))))