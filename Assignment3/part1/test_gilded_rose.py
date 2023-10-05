# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # Refactor this example test case
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def helper(self, items, days):
        for day in range(days):
            print("-------- day %s --------" % day)
            print("name, sellIn, quality")
            for item in items:
                print(item)
            print("")
            GildedRose(items).update_quality()

    # Test the quality degrades twice as fast as date passed
    def test_past_date(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=3, quality=20)]
        days = 6
        self.helper(items, days)
        self.assertEquals(-3, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    def test_quality_non_negative(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=5, quality=3)]
        days = 5
        self.helper(items, days)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_aged_brie(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=0)]
        days = 5
        self.helper(items, days)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(5, items[0].quality)

    def test_quality_upper_limit(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=49)]
        days = 5
        self.helper(items, days)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_sulfuras(self):
        items = [
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                ]
        days = 3
        self.helper(items, days)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(-1, items[1].sell_in)
        self.assertEquals(80, items[0].quality)
        self.assertEquals(80, items[1].quality)

    def test_backstage_passes(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=30)]
        days = 17
        self.helper(items, days)
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_conjured(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        days = 3
        self.helper(items, days)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
