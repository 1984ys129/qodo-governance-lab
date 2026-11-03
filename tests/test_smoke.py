import unittest

from catalog.service import list_page, quote_total


class SmokeTests(unittest.TestCase):
    def test_single_page(self):
        self.assertEqual(list_page(["a"], 0, 10), (["a"], None))

    def test_single_item_quote(self):
        self.assertEqual(quote_total(1000, 1, 1000), 900)


if __name__ == "__main__":
    unittest.main()
