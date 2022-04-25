from Model import Item


class Storerepository:

    def __init__(self):

        self.Products = Item.query.all()

    def get_products(self):
        return self.Products

    def get_products_by_category(self, category):

        orderedproducts = []
        products = self.Products

        for product in products:
            if product.category == category:
                orderedproducts.append(product)

        return orderedproducts

    def get_product_by_name(self, name):

        products = self.Products

        for product in products:
            if product.name == name:
                return product
