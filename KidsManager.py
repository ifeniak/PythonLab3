from Item import Item
from CreativityType import CreativityType
from Order import Order


class KidsManager:

    def __init__(self, *goods: Item):
        self.goods = list(goods)

    def search_by_type(self, creativity_type: CreativityType):
        searched = []
        for x in self.goods:
            if x.creativity_type == creativity_type:
                searched.append(x)
        return searched

    def sort_by_name(self, order: Order):
        if order == Order.DESC:
            return sorted(self.goods, key=lambda goods: goods.name, reverse=True)
        return sorted(self.goods, key=lambda goods: goods.name, reverse=True)

    def sort_by_price(self, order: Order):
        if order == Order.DESC:
            return sorted(self.goods, key=lambda goods: goods.price, reverse=True)
        return sorted(self.goods, key=lambda goods: goods.price, reverse=True)
