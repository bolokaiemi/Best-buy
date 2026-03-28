class Store:
    def __init__(self, products):
        # list of Product objects
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        # return only active products
        return [product for product in self.products if product.is_active()]

    @staticmethod
    def order(shopping_list) -> float:
        total_price = 0.0

        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"{product.name} is not active!")

            # use Product.buy()
            total_price += product.buy(quantity)

        return total_price