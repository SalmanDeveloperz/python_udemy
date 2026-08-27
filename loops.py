mist= [1,2,3,4,5,6,7,8]

new=0
for i in mist:
    new +=i
print(new)

mist2=["Monday", "Tuesday", "Wednesday", "Thursday","Friday"]
for i in mist2:
    print(f"Happy {i}")


j=0
while j<5:
    j+=1
    if j==3:
        continue
    print(f"Happy{j}")
