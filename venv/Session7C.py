x = 10

def fun():
    global x
    x = 21
    x = x + 1
    print("x in fun is:",x)

fun()
fun()

print("x finally is: ",x) # 22
