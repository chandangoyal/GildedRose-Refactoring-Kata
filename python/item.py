from abc import ABC, abstractmethod

from python.helper import decrease_quality, increase_quality


class Item(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update_quality(self):
        """Update the quality of an item"""
        pass


class RegularItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        """Update the quality of an item"""
        self.quality = decrease_quality(quality=self.quality, sell_in=self.sell_in)
        self.sell_in = self.sell_in - 1


class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        pass


class Backstage(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality = increase_quality(quality=self.quality, increase_quality_by=3)
        elif self.sell_in <= 10:
            self.quality = increase_quality(quality=self.quality, increase_quality_by=2)
        else:
            self.quality = increase_quality(quality=self.quality)
        self.sell_in = self.sell_in - 1


class AgedBrie(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = increase_quality(quality=self.quality)
        self.sell_in = self.sell_in - 1


class Conjured(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = decrease_quality(quality=self.quality, sell_in=self.sell_in, decrease_quality_by=2)
        self.sell_in = self.sell_in - 1
