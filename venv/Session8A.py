def fun(**kwargs):
    print(kwargs)

print("fun is:",fun)

# Re-Creating a new function fun and overwriting old one !!
def fun(*args, **kwargs):
    print(args)
    print(kwargs)


print("fun now is:",fun)
fun(10, 20, 30, a=10, b=20, c=30)


"""
def fun(*args, **kwargs, *args1):
    pass

fun(10, 20, 30, a=10, b=20, c=30, 1, 2, 3)
"""