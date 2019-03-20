x = 10

def fun():
    global x
    x = 21
    x = x + 1
    print("x in fun is:",x)

fun()
fun()

print("x finally is: ",x) # 22

# Assignment:
# Create a Function which simulates Promo Codes as in Zomato/Amazon/Uber/OLA
"""
    def getFinalPriceAfterPromoCode(amount, promoCode):
        ..
        ..
        ....
        ......
        return 

"""
