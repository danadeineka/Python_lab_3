from .country import Country
from .tools import Tools
from .material import Material


class GroundTools(Tools):
    def __init__(self, name: str, weight: int, price: float, material: Material, country: Country, user: str,
                 version: str):
        super().__init__(name, weight, price, material, country, user)
        self.version = version

    def __del__(self):
        pass

    def __str__(self):
        return super(GroundTools, self).__str__() + f'Sensivity: {self.version}\n'

    @property
    def get_version(self):
        return self.version
