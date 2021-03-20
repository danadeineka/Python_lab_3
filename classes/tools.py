from classes.country import Country
from classes.material import Material


class Tools:
    def __init__(self, name: str, weight: int, price: float, material: Material, country: Country,
                 user: str):
        self.name = name
        self.weight = weight
        self.price = price
        self.material = material
        self.country = country
        self.user = user

    def __del__(self):
        pass

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Weight in grams: {self.weight}\n' \
               f'Price in dollars: {self.price}\n' \
               f'Material: {self.material}\n' \
               f'Country: {self.country}\n' \
               f'User: {self.user}\n'
