import unittest
from array_list import ArrayList, how_many  # assuming these are the functions/classes you want to test

class TestArrayList(unittest.TestCase):
    def test_insert(self):
        arr_list = ArrayList()
        arr_list.insert(5, 0)
        self.assertEqual(str(arr_list), '5 0 0 0 0')  # assuming str representation of arr_list is '5 0 0 0 0'

    def test_how_many(self):
        result = how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result, 2)

# add more test cases as needed

if __name__ == '__main__':
    unittest.main()