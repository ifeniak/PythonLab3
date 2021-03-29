from CreativityType import CreativityType
from Country import Country


class Item:

    def __init__(self, name, brand_country: Country, origin_country: Country, brand, price, recommended_age: list,
                 creativity_type: CreativityType):
        self.name = name
        self.brand_country = brand_country
        self.origin_country = origin_country
        self.brand = brand
        self.price = price
        self.recommended_age = recommended_age
        self.creativity_type = creativity_type

    def __repr__(self):
        return f'name: {self.name}\n' \
               f'brand_country: {self.brand_country}\n' \
               f'origin_country: {self.origin_country}\n' \
               f'brand: {self.brand}\n' \
               f'price: {self.price}\n' \
               f'recommended_age: {self.recommended_age}\n' \
               f'creativity_type: {self.creativity_type}\n'
