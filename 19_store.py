"""
Create class STORE to keep track of products (Product Code, Name and price).
Display menu of all prodcuts to user, Generate bill as per order.
"""
class Product:
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price

class store:

    def __init__(self):
        self.product_list = []
        self.cart = []

    # ADD PRODUCT TO DISPLAY LIST    
    def add(self, product):
        self.product_list.append(product)
    
    # DISPLAY ITEMS IN THE STORE
    def display(self):
        for product in self.product_list:
            print(product.product_code, product.name, product.price)

    # ADD ITEMS TO CART BASED ON PRODUCT CODE       
    def add_to_cart(self, product):
        for item in self.product_list:
            if item.product_code == product:
                self.cart.append(item)
                print("ADDED ITEM")
                return
        print("INVALID ITEM")

    # REMOVE ITEMS FROM CART BASED ON PRODUCT CODE
    def remove_from_cart(self, product):
        for item in self.cart:
            if item.product_code == product:
                self.cart.remove(item)
                print(f'{item.name} removed from cart')
                return
        print("NO PRODUCT FOUND IN CART WITH THIS CODE")

    # GENERATE BILL FROM ITEMS PRESENT IN CART
    def generate_bill(self):
        amount = 0
        for product in self.cart:
            amount += product.price
        print("TOTAL BILL AMOUNT IS", amount)
        print("HAPPY SHOPPING!")

    # DISPLAY ITEMS IN CART
    def display_cart(self):
        print("Your cart contains: \n")
        for item in self.cart: 
            print(item.name)

# ADDING PRODUCTS TO STORE
# ADD MORE USING THE FORMAT (PRODUCT_CODE,PRODUCT_NAME,PRICE)
s = store()
s.add(Product(1,"CHOCOLATE",50))
s.add(Product(2,"CHIPS",20))
s.add(Product(3,"COFFEE",60))


# DISPLAY OPTIONS TO USER
a = 1
while a == 1: 
    print(" \n 1.DISPLAY PRODUCTS \n 2.ADD PRODUCT TO CART \n 3.REMOVE PRODUCT \n 4.VIEW CART \n 5.GENERATE BILL \n 6.EXIT ")
    choice = int(input("Enter Your choice:"))

    if choice == 1:
        s.display()
    elif choice == 2:
        code = int(input("Enter product code: "))
        s.add_to_cart(code)
    elif choice == 3:
        code = int(input("Enter Product code: "))
        s.remove_from_cart(code)
    elif choice == 4:
        s.display_cart()
    elif choice == 5:
        s.generate_bill()
        exit()
    elif choice == 6:
        exit()
    else:
        print("Enter a valid choice")

# GITHUB: yxsh7

