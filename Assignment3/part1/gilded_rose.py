# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    """
    In the refactored code, I applied the "Strategy Pattern", which is a behavioral design pattern.
    This pattern can define a family of algorithms, encapsulate each one of them, and make them interchangeable.
    """
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    # Increase quality by certain val each day, up to 50
    def increase_quality_by(self, val, item):
        item.quality = min(item.quality + val, 50)

    # Drop quality depends on sell date. Once the sell by date has passed, Quality degrades twice as fast. Down to 0.
    def drop_quality_by(self, val, item, days):
        if days > 0:
            item.quality = max(item.quality - val, 0)
        else:
            item.quality = max(item.quality - val * 2, 0)

    def update_quality(self):
        for item in self.items:
            # Ignore the Sulfuras items
            if "Sulfuras" in item.name:
                continue

            # Aged Brie quality increased by date, up to 50
            if item.name == "Aged Brie":
                self.increase_quality_by(1, item)
            # Check different cases for backstage passes
            elif "Backstage passes" in item.name:
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    self.increase_quality_by(3, item)
                elif item.sell_in <= 10:
                    self.increase_quality_by(2, item)
                else:
                    self.increase_quality_by(1, item)
            # Conjured items
            elif "Conjured" in item.name:
                self.drop_quality_by(2, item, item.sell_in)
            # General cases
            else:
                self.drop_quality_by(1, item, item.sell_in)

            # decrease sell date by 1 each day
            item.sell_in -= 1
