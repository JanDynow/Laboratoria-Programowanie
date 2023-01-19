# Napisz program sumujący wartości parzyste listy. Policzoną sumę wstaw jako nowy element na początku
# listy.

l=[1,2,3,4,5,6,7,8,9,10]
print("lista przed policzeniem liczb parzystych: ", l)
x = 0
for i in l:
    a = i%2
    if a == 0:
        x += 1
    else:
        x += 0
l.insert(0,x)

print("Lista po policzeniu liczb parzystych", l)






