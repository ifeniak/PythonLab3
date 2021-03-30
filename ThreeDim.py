from Item import Item
from Material import Material


class ThreeDim(Item):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, power_supply, *materials: Material):
        super().__init__(name, brand_country, origin_country, brand, price, recommended_age, creativity_type)
        self.power_supply = power_supply
        self.materials = materials

    def __repr__(self):
        return super().__repr__() + f'power_supply: {self.power_supply}\n' + f'materials: {self.materials}\n'
