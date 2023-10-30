import unittest
from LAB6_2 import search_min_element_index

a = [-1, 48, 50, 14, -5, -7, -6, 45, 30, -2, -2, -28, 15, -26, -33, -15, 10, -35, -16, 46, 46, -14]


class TestMinElementIndex(unittest.TestCase):
    def test_search_min_element_index(self):
        self.assertEqual(search_min_element_index(a), 11)  # add assertion here


if __name__ == '__main__':
    unittest.main()
