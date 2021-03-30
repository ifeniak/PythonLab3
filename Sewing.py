from Item import Item
from Colour import Colour


class Sewing(Item):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, number_of_needles, threads_color: Colour):
        super().__init__(name, brand_country, origin_country, brand, price, recommended_age, creativity_type)
        self.number_of_needles = number_of_needles
        self.threads_color = threads_color

    def __repr__(self):
        return super().__repr__() + f'number_of_needles: {self.number_of_needles}\n' +\
               f'threads_color: {self.threads_color}\n'
