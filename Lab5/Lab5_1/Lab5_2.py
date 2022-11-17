sample_dict = {"name": "Kelly", "surname": "Jones", "age": 25, "salary": 8000, "city": "New York"}
print(sample_dict)
for k,v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')

L = ["name", "age"]
D = {}
for i in L:
    for j in sample_dict.keys():
        if i == j:
            D[i] = sample_dict[j]
            break

print(D)
L = ["name", "age"]
for k in L:
    if k in sample_dict.keys():
        sample_dict.pop(k)
print(sample_dict)

for k in sample_dict.values():
    if k == "Jones":
        print("istnieje")
        break
else:
    print("nie istnieje")

