class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product_name, price, quantity=1):
        if product_name not in self.cart:
            self.cart[product_name] = {"price": price, "quantity": quantity}
        else:
            print("already exist.")

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
        else:
            print("doesn't exist")

    def update_product(self, product_name, price=None, quantity=None):
        if product_name in self.cart:
            if price is not None:
                self.cart[product_name]["price"] = price
            if quantity is not None:
                self.cart[product_name]["quantity"] = quantity
        else:
            print("doesn't exist")

    def unique_products(self):
        return len(self.cart)

    def total_price(self):
        total = 0
        for product in self.cart.values():
            total += product["price"] * product["quantity"]
        return total


cart = ShoppingCart()

while True:
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Total Unique Products")
    print("5. Total Price")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == 1:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        cart.add_product(product_name, price, quantity)
        print("Product added to cart.")

    elif choice == 2:
        product_name = input("Enter name to remove: ")
        cart.remove_product(product_name)
        print("Product removed from cart.")

    elif choice == 3:
        product_name = input("Enter product name to update: ")
        price = input("Enter new price: ")
        if price:
            price = float(price)
        quantity = input("Enter new quantity: ")
        if quantity:
            quantity = int(quantity)
        cart.update_product(product_name, price, quantity)
        print("Product updated.")

    elif choice == 4:
        print("Total unique products:", cart.unique_products())

    elif choice == 5:
        print("Total price:", cart.total_price())

    elif choice == 6:
        print("Exiting")
        break

    else:
        print("Invalid choice!!")