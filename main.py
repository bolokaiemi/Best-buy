import products
import store


def start(best_buy):
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
        """)

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            print("------")
            product_list = best_buy.get_all_products()
            for i, product in enumerate(product_list, start=1):
                print(f"{i}. {product}")
            print("------")

        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total of {total} items in store")

        elif choice == "3":
            product_list = best_buy.get_all_products()

            print("------")
            for i, product in enumerate(product_list, start=1):
                print(f"{i}. {product}")
            print("------")

            print("When you want to finish order, enter empty text.")
            shopping_list = []

            while True:
                choice = input("Which product # do you want? ").strip()
                if choice == "":
                    break

                amount = input("What amount do you want? ").strip()

                # strict validation (matches your output)
                if (not choice.isdigit() or
                    int(choice) < 1 or
                    int(choice) > len(product_list) or
                    not amount.isdigit()):
                    print("Error adding product!")
                    continue

                product = product_list[int(choice) - 1]
                amount = int(amount)

                shopping_list.append((product, amount))
                print("Product added to list!")

            try:
                total_price = best_buy.order(shopping_list)
                if shopping_list:
                    print(f"Order made! Total price: ${total_price}")
            except Exception as e:
                print(f" Error placing order: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Enter a number 1-4.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()