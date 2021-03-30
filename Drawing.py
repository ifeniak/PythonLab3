from Item import Item


class Drawing(Item):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, power_supply, number_of_brushes):
        super().__init__(name, brand_country, origin_country, brand, price, recommended_age, creativity_type)
        self.number_of_brushes = number_of_brushes

    def __repr__(self):
        return super().__repr__() + f'number_of_brushes: {self.number_of_brushes}\n'
