#Q24 - Product Discount System
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self):
        return self.price - (self.price * 10 / 100)


product = Product("Laptop", 100000)

print("Product:", product.name)
print("Original Price:", product.price)
print("Discounted Price:", product.discount())