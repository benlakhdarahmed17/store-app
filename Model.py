

from email.mime import image


class Product:

    def __init__(self, name, quantity, category, description, image):
        self.name = name
        self.quantity = int(quantity)
        self.category = category
        self.description = description
        self.image = image
        self.cart = False
