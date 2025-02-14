# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_backstage_passes_to_a_TAFKAL80ETC_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality, "Backstage passes should increase 3 quality daily when less than 5 days")

    def test_conjured_before_expiration(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality, "Conjured items should lose 2 quality daily before expiration")

    def test_conjured_after_expiration(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality, "Conjured items should lose 4 quality daily after expiration")

    def test_get_all_item_names(self):
        items = [
            Item("foo", 0, 3),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 45),
            Item("Conjured Mana Cake", 3, 6)
        ]
        gilded_rose = GildedRose(items)
        names = gilded_rose.get_all_item_names()
        expected_names = ["foo", "Backstage passes to a TAFKAL80ETC concert", "Conjured Mana Cake"]
        self.assertEqual(expected_names, names)


if __name__ == '__main__':
    unittest.main()
