a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a2 = []

print(type(a1))
# print(type(a2))

print("Original Values")
print(a1)
# print(a2)
print()

# for i in range(len(a1)):
#     a2.append(a1[i])

a2 = [i + 1 for i in range(len(a1))]

print("Copied from a1 to a2")
print(a1)
print(a2)
print()

print("Add to a1")
a1.append(10)
print(a1)
print(a2)
print()

print("Add to a1")
a1.append(11)
print(a1)
print(a2)
print()

print("add to a2")
a2.append(10)
print(a1)
print(a2)
print()

print(id(a1))
print(id(a2))
print(type(a1[0]))
print(type(a2))

food = [['apple', 'banana', 'mango'], ['corn', 'carrot', 'celery']]

print(food)

fruits = food[0]
vegetables = food[1]

print(fruits)
print(vegetables)

print(f"{food[0][1]} is equal to {fruits[1]}? {food[0][1]==fruits[1]}")