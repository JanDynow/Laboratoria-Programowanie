
def function(*args):
    print(*args)
    for i in args:
        print(i)
function(1,1.5,False,[2,6])

def max(numer1,*args):
    print(numer1,*args)
    a = numer1
    for z in args:
        if z>a:
            a = z
    return a
print(max(66,2,3,-5,32,44,22))
