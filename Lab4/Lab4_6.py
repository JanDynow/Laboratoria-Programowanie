X = list(range(10))
print(X)
X[:0] = X[-3:]
#del X[-3:]
X[-3:] = []
print(X)

Y = X[:]
Y[4] = 50
print(X)
print(Y)













