# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    def __init__(self, item: Item):
        self.item = item

    def update(self):
        raise NotImplementedError("Subclasses must override update() method.")


class RegularUpdater(ItemUpdater):
    def update(self):
        self.decrease_quality(1)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.decrease_quality(1)

    def decrease_quality(self, amount):
        self.item.quality = max(0, self.item.quality - amount)


class AgedBrieUpdater(ItemUpdater):
    def update(self):
        self.increase_quality(1)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.increase_quality(1)

    def increase_quality(self, amount):
        self.item.quality = min(50, self.item.quality + amount)


class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass


class BackstageUpdater(ItemUpdater):
    def update(self):
        if self.item.sell_in > 10:
            self.increase_quality(1)
        elif self.item.sell_in > 5:
            self.increase_quality(2)
        elif self.item.sell_in >= 0:
            self.increase_quality(3)
        else:
            self.item.quality = 0

        self.item.sell_in -= 1

    def increase_quality(self, amount):
        self.item.quality = min(50, self.item.quality + amount)


class ConjuredUpdater(RegularUpdater):
    def update(self):
        self.decrease_quality(2)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.decrease_quality(2)


def get_updater(item: Item) -> ItemUpdater:
    if item.name == "Aged Brie":
        return AgedBrieUpdater(item)
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater(item)
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstageUpdater(item)
    elif "Conjured" in item.name:
        return ConjuredUpdater(item)
    else:
        return RegularUpdater(item)


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = get_updater(item)
            updater.update()

    def get_all_item_names(self):
        return [item.name for item in self.items]