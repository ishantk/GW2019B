num = 21

def show(n):
    # global num -> error

    num = num * 3
    print("num is:",num)

x = 10
show(x)

print("show is:",show)  # HashCode
print("x is:",x)        # 10
print("num is:",num)    # 63/21/10