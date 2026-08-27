my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

print (f"{my_vehicle}\n")
for i,j in my_vehicle.items():
    print (i,j)

print("---------------------\n")

vehicle2= my_vehicle.copy()
vehicle2.update({
    "number_of_tires": "4"
})
for i,j in vehicle2.items():
    print (i,j)

print("---------------------\n")

vehicle2.pop("mileage")

for i,j in vehicle2.items():
    print(i,j)