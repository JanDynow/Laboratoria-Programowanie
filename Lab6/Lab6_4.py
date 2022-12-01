def fun(**kwargs):
    for key, item in kwargs.items():
        print("Nazwa: ", key, "Argument: ", item)
fun(a="end", b=12)

