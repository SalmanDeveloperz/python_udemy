"""

Lists Assignment
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

"""

zoo_list=["lion","deer","monkey","elephant","eagle"]
print(zoo_list)

print("\nDelete the animal at the 3rd index: ")
zoo_list.pop(3)
print(zoo_list)

print("\nAppend a new animal at the end of the list: ")
zoo_list.append("Tiger")
print(zoo_list)

print(f"\nDelete the animal at the beginning of the list:")
zoo_list.pop(0)

print(zoo_list)

print(f"\nPrint onlyt the first 3 animals:")
print(zoo_list[0:3])
