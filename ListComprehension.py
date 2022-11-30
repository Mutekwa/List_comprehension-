# simple loop to print the items in a list
fruits = ["apples", "pineapples", "oranges"]

for fruit in fruits:
    print(fruit)

# with list comprehension just a simple one line of code
[print(fruit) for fruit in fruits]

# to change the items in a list to upper case
animals = ["lion", "giraffe", "elephant"]
# new_animals = []
# for animal in animals:
#     new_animals.append(animal.upper())
# print(new_animals)

# with list comprehension
# we dont need to declare a new list since the list comprehension does it for us
# thats why we start our list comprehension code inside the square brackets
# append is notoriously known for its slow pace while list comprehension is fast with larger input

animals = [animal.upper() for animal in animals]
print(animals)

bits = [True, True, False, True, True, False, False, True, False]
new_bits = []
for bit in bits:
    if bit == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(bits)
print(new_bits)

# with list comprehension
super_bits = [1 if bit == True else 0 for bit in bits]
print(super_bits)

# String Manipulation
strings = "HillaryAmbetsaMutekwa"
strings = "".join([i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in strings])[1:]
print(strings)
