import unittest
from array_list import ArrayList, Empty

class ArrayListTests(unittest.TestCase):
    def test_get_last_with_items(self):
        # Arrange
        arr_list = ArrayList()
        arr_list.append(10)
        arr_list.append(20)
        arr_list.append(30)

        # Act
        result = arr_list.get_last()

        # Assert
        self.assertEqual(result, 30)

    def test_get_last_empty_list(self):
        # Arrange
        arr_list = ArrayList()

        # Act & Assert
        with self.assertRaises(Empty):
            arr_list.get_last()

if __name__ == '__main__':
    unittest.main()