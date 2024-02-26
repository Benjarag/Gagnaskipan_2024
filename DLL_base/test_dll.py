import unittest
from dll import DoublyLinkedList

class PartitionTests(unittest.TestCase):
    def test_partition(self):
        # Arrange
        dll = DoublyLinkedList()
        elements = [10, 7, 7, 14, 10, 15, 1, 8, 2, 4, 13, 7, 11, 8, 8, 13]
        for element in elements:
            dll.append(element)
        
        # Act
        dll.partition(dll.get_first_node(), dll.get_last_node())

        # Assert
        expected = [7, 7, 1, 8, 2, 4, 7, 8, 8, 10, 14, 10, 15, 13, 11, 13]
        actual = [node.data for node in dll]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()