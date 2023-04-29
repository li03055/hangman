def print_products(products):
    print("Products: ")
    for product in products:
        print(product)
        print('\n')

def print_product_count(products):
    print("Number of products: ", len(products))

def is_product_on_list(products, product):
    if product in products:
        print(product, " is on the list")
    else:
        print(product, " is not on the list")

def count_product_occurrences(products, product):
    count = products.count(product)
    print(product, "appears", count, "times in the list")

def remove_product(products, product):
    if product in products:
        products.remove(product)
        print(product, " removed from the list")
    else:
        print(product, " is not on the list")

def add_product(products, product):
    if product not in products:
        products.append(product)
        print(product, "added to the list")
    else:
        print(product, "is already on the list")

def print_invalid_products(products):
    invalid_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    if len(invalid_products) > 0:
        print("Invalid products: ")
        for product in invalid_products:
            print(product)
    else:
        print("There are no invalid products in the list")

def remove_duplicates(products):
    unique_products = list(set(products))
    products.clear()
    products.extend(unique_products)
    print("Duplicates removed from the list")

def get_valid_input():
    while True:
        user_input = input("Please enter a number between 1 and 9: ")
        if user_input.isdigit() and int(user_input) in range(1, 10):
            return int(user_input)

def get_valid_product_name():
    while True:
        product_name = input("Please enter a product name: ")
        if len(product_name) >= 3 and product_name.isalpha():
            return product_name

def main():
    products_str = input("Please enter a list of products (without spaces): ")
    products = products_str.split(",")

    while True:
        print("\nChoose a number: ")
        print("\n1. Print list")
        print("\n2. Print number of products in list")
        print("\n3. Check if a product is on the list")
        print("\n4. Count the number of times a product is in list")
        print("\n5. Remove a product from list")
        print("\n6. Add a product to list")
        print("\n7. Print invalid products")
        print("\n8. Remove duplicates from list")
        print("\n9. Exit")

        choice = get_valid_input()

        if choice == 1:
            print_products(products)
        elif choice == 2:
            print_product_count(products)
        elif choice == 3:
            product = get_valid_product_name()
            is_product_on_list(products, product)
        elif choice == 4:
            product = get_valid_product_name()
            count_product_occurrences(products, product)
        elif choice == 5:
            product = get_valid_product_name()
            remove_product(products, product)
        elif choice == 6:
            product = get_valid_product_name()
            add_product(products, product)
        elif choice == 7:
            print_invalid_products(products)
        elif choice == 8:
            remove_duplicates(products)
        else:
            break

    print("Goodbye!")

if __name__ == '__main__':
    main()
