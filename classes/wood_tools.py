from .country import Country
from .tools import Tools
from .material import Material
from .size import Size


class WoodTools(Tools):
    def __init__(self, name: str, weight: int, price: float, material: Material, country: Country,
                 user: str, size: Size):
        super().__init__(name, weight, price, material, country, user)
        self.size = size

    def __del__(self):
        pass

    def __str__(self):
        return super(WoodTools, self).__str__() + f'Speed: {self.size}\n'
