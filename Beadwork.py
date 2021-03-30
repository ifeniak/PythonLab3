from Sewing import Sewing
from Colour import Colour


class Beadwork(Sewing):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type,
                 number_of_needles, threads_color, *beads_color: Colour):
        super().__init__(name, brand_country, origin_country, brand, price,
                         recommended_age, creativity_type, number_of_needles, threads_color)
        self.beads_color = beads_color

    def __repr__(self):
        return super().__repr__() + f'beads_color: {self.beads_color}\n'
