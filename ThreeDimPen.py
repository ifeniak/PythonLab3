from ThreeDim import ThreeDim
from Colour import Colour


class ThreeDimPen(ThreeDim):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, power_supply, *materials, ink_material, color: Colour):
        super().__init__(name, brand_country, origin_country, brand,
                         price, recommended_age, creativity_type, power_supply, *materials)
        self.ink_material = ink_material
        self.color = color

    def __repr__(self):
        return super().__repr__() + f'ink_material: {self.ink_material}\n' + f'color: {self.color}\n'
