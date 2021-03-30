from ThreeDim import ThreeDim


class DrawingBoard(ThreeDim):

    def __init__(self, name, brand_country, origin_country, brand,
                 price, recommended_age: list, creativity_type, power_supply, *materials, backlight_type):
        super().__init__(name, brand_country, origin_country, brand,
                         price, recommended_age, creativity_type, power_supply, *materials)
        self.backlight_type = backlight_type

    def __repr__(self):
        return super().__repr__() + f'backlight_type: {self.backlight_type}\n'
