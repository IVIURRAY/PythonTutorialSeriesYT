# If statements and conditions
x = 19

if x > 18:
    print('You are above 18 years old!')
elif x > 10 and x <= 18:
    print('You are greater than 10 and 18 or less years old!')
else:
    print('You are below 10 years!')

# Ternary
print('I am older than 18') if x > 18 else print('I am 18 or less')

# Booleans
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False
