# "Joe", "Sally", "Jim", "June", "Betty", "Bill", "Sara", "Zak", "Anne", "Kate"

names = []

for x in range(10):
    names.append(input("Enter Name: "))

print(names)

for x in range(10):
    print(names.pop(0))

if len(names) == 0:
    print("[]")

print(names)


