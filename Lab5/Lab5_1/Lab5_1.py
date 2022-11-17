#zadanie 1
values = [10,20,30]
keys = ["ten", "twenty", "thirty"]

D = dict(zip(keys, values))
print(D)




Z = dict(thirty = 30, forty = 40, fifty = 50)
print(Z)
D.update(Z)
print(D)



