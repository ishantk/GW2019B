class Order:

    def __init__(self, oid, customer, restaurant, price):
        self.oid = oid
        self.customer = customer
        self.restaurant = restaurant
        self.price =price

    def showOrder(self):
        print("===Order===")
        print("Order Id:",self.oid)
        print("Customer:",self.customer)
        print("Restaurant:", self.restaurant)
        print("Price: \u20b9", self.price)
        print("===========")

    def applyPromoCode(self, promoCode):
        pass


o1 = Order(1, "John", "ABC Kitchen", 3000)
o1.showOrder()

# 1. Collection of Orders
# 2. Sort the list of orders on the basis of price (Desc)
# 3. Sum up all the prices and show what was total earning
# 4. PromoCode : ABC20, XYZ50 | * price > 500 < 1000 for ABC20 | price >= 1000 | XYZ50
