from abc import ABC

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

class Account(ABC):
    products_list = []
    seller_data = []
    customer_data = []

    def __init__(self, name, email, password):
        self.name = name
        self.__email = email
        self.__password = password

    def check_credentials(self, email, password):
        return self.__email == email and self.__password == password

    @property
    def email(self):
        return self.__email

class Customer(Account):
    def new_customer_account(self, customer):
        Account.customer_data.append(customer)
        print(f"Customer added: {customer.email}")

    def log_in(self, email, password):
        for customer in Account.customer_data:
            if customer.check_credentials(email, password):
                print("Customer log in success...")
                return True, customer
        print("Wrong customer email or password")
        return False, None

    def show_products(self):
        print(f"Name   Price   Quantity")
        for product in Account.products_list:
            if product.quantity > 0:
                print(f"{product.name} - {product.price} - {product.quantity}")

    def place_order(self, name, qty):
        for product_item in Account.products_list:
            if name == product_item.name:
                if product_item.quantity >= qty > 0:
                    total_amount = qty * product_item.price
                    print(f"Thank you for your purchase! Your total amount: {total_amount}")
                    product_item.quantity -= qty
                    return
                else:
                    print(f"We only have {product_item.quantity} quantity")
                    return
        print("Wrong product name")

class Product_item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Seller(Account):
    def add_product(self, product_item):
        Account.products_list.append(product_item)
        print(f"Product Added: {product_item.name} - {product_item.price}")

    def new_account(self, seller):
        Account.seller_data.append(seller)
        print(f"Seller added: {seller.email}")

    def log_in(self, email, password):
        for seller in Account.seller_data:
            if seller.check_credentials(email, password):
                print("Seller log in success...")
                return True, seller
        print("Wrong seller email or password")
        return False, None


#-------Main Program ------#
print("-----Welcome to online shopping-----")

while True:
    print("\n1. Seller\n2. Customer\n3. Exit")
    choice = input_int("Enter any number 1-3: ")

    if choice == 1:
        print("\n1. Log in\n2. Create new account\n3. Exit")
        seller_choice = input_int("Enter number: ")

        if seller_choice == 1:
            email = input("Email: ")
            password = input("Password (numbers only): ")
            if not password.isdigit():
                print("Password must be a number.")
                continue
            password = int(password)
            seller = Seller("", "", 0)
            is_valid, logged_seller = seller.log_in(email, password)
            if is_valid:
                while True:
                    print("\n1. Add product\n2. Logout")
                    action = input_int("Enter: ")
                    if action == 1:
                        name = input("Product Name: ")
                        price = input("Price (numbers only): ")
                        if not price.isdigit():
                            print("Price must be a number.")
                            continue
                        price = int(price)
                        qty = input("Quantity (numbers only): ")
                        if not qty.isdigit():
                            print("Quantity must be a number.")
                            continue
                        qty = int(qty)
                        product = Product_item(name, price, qty)
                        logged_seller.add_product(product)
                    elif action == 2:
                        print("Logged out.")
                        break
                    else:
                        print("Wrong input")
            else:
                print("Login failed")

        elif seller_choice == 2:
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password (numbers only): ")
            if not password.isdigit():
                print("Password must be a number.")
                continue
            password = int(password)
            new_seller = Seller(name, email, password)
            new_seller.new_account(new_seller)

        elif seller_choice == 3:
            break

        else:
            print("Wrong input")

    elif choice == 2:
        print("\n1. Create new account\n2. Log in\n3. Exit")
        customer_choice = input_int("Enter number: ")

        if customer_choice == 1:
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password (numbers only): ")
            if not password.isdigit():
                print("Password must be a number.")
                continue
            password = int(password)
            new_customer = Customer(name, email, password)
            new_customer.new_customer_account(new_customer)

        elif customer_choice == 2:
            email = input("Email: ")
            password = input("Password (numbers only): ")
            if not password.isdigit():
                print("Password must be a number.")
                continue
            password = int(password)
            customer = Customer("", "", 0)
            is_valid, logged_customer = customer.log_in(email, password)
            if is_valid:
                while True:
                    print("\n1. View products\n2. Order\n3. Logout")
                    action = input_int("Enter number: ")
                    if action == 1:
                        logged_customer.show_products()
                    elif action == 2:
                        name = input("Product name to order: ")
                        qty = input("Quantity (numbers only): ")
                        if not qty.isdigit():
                            print("Quantity must be a number.")
                            continue
                        qty = int(qty)
                        logged_customer.place_order(name, qty)
                    elif action == 3:
                        print("Logged out.")
                        break
                    else:
                        print("Wrong input")
            else:
                print("Login failed")

        elif customer_choice == 3:
            break

        else:
            print("Wrong input")

    elif choice == 3:
        print("Thank you for visiting!")
        break

    else:
        print("Wrong input")
