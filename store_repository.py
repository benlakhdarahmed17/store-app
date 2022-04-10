from Model import Product


class Storerepository:

    def __init__(self):

        self.products = [
            Product('Underwear', '10', 'Clothes',
                    'Some text about underwear', 'underwear'),
            Product('Footwear', '5', 'Clothes',
                    'Some text about footwear', 'footwear'),
            Product('Fromage', '20', 'Food',
                    'Some text about fromage', 'fromage'),
            Product('Whey protein', '6', 'Food',
                    'Some text about whey', 'whey'),
            Product('TV', '3', 'Home', 'Some text about tvs', None),
            Product('Washing Machine', '3', 'Home',
                    'Some text about washing machine', None),
            Product('home Barfix', '2', 'Gym',
                    'Some text about home equipement', None),
            Product('Wheight Disks', '15', 'Gym',
                    'Some text about workout discs', None),
        ]
        self.cart = []

    def get_products(self):
        return self.products

    def get_products_by_category(self, category):

        orderedproducts = []
        products = self.products

        for product in products:
            if product.category == category:
                orderedproducts.append(product)

        return orderedproducts

    def get_product_by_name(self, name):

        products = self.products

        for product in products:
            if product.name == name:
                return product
