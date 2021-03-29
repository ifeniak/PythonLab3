from Item import Country, CreativityType
from ThreeDim import Material
from ThreeDimPen import ThreeDimPen, Colour
from DrawingBoard import DrawingBoard
from Beadwork import Beadwork
from ToyKnitting import ToyKnitting, ToyFiller
from KidsManager import KidsManager
from Order import Order


def main():
    item1 = ThreeDimPen('3D-pen', Country.EU, Country.OTHERS, 'br1', 11.1, [10, 11], CreativityType.THREE_DIM, 'ac',
                        Material.METAL, ink_material='blood', color=Colour.VIOLET)
    item2 = DrawingBoard('Draw on Board', Country.USA, Country.EU, 'br1', 29, [5, 6, 7], CreativityType.DRAWING, 'usb',
                         Material.METAL, backlight_type='neon')
    item3 = Beadwork('Bead workers', Country.CHINA, Country.EU, 'br1', 148, [9, 14], CreativityType.SEWING, 9,
                     Colour.RED, Colour.RED, Colour.BLUE)
    item4 = ToyKnitting('Toy Creating', Country.EU, Country.OTHERS, 'br1', 20000, [12], CreativityType.SEWING, 9,
                        Colour.GREEN, toy_filler=ToyFiller.LINEN)

    kids_manager = KidsManager(item1, item2, item3, item4)
    print(kids_manager.search_by_type(CreativityType.SEWING), '\n\n\n')
    print(kids_manager.sort_by_name(Order.ASC), '\n\n\n')
    print(kids_manager.sort_by_price(Order.DESC), '\n\n\n')


if __name__ == '__main__':
    main()
