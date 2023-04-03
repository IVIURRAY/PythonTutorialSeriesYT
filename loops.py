# For Loop
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)

count = 0
while count < 6:
    print(count)
    count = count + 1

for number in numbers:
    if number == 3:
        break
    print(number)

for number in numbers:
    if number == 3:
        continue
    print(number)

names = ['bob', 'sally', 'jane', 'fred']
for i, name in enumerate(names):
    print(i, name)

result = []
for number in numbers:
    if number > 3:
        result.append(number)
print(result)

result = [number for number in numbers if number > 3]
print(result)
