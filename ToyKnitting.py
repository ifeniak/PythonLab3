from Sewing import Sewing
from ToyFiller import ToyFiller


class ToyKnitting(Sewing):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, number_of_needles, threads_color,
                 toy_filler: ToyFiller):
        super().__init__(name, brand_country, origin_country, brand,
                         price, recommended_age, creativity_type, number_of_needles, threads_color)
        self.toy_filler = toy_filler

    def __repr__(self):
        return super().__repr__() + f'toy_filler: {self.toy_filler}\n'