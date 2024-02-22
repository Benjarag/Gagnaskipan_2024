import unittest
from kennslustund_10_20feb import Node, SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SingleLinkedList()

    def test_empty_list(self):
        self.assertEqual(self.list.length_of_list(), 0)
        self.assertEqual(str(self.list), "[]")

    def test_add_node(self):
        self.list.add_node(10)
        self.assertEqual(self.list.length_of_list(), 1)
        self.assertEqual(str(self.list), "[10]")

    def test_remove_node(self):
        self.list.add_node(10)
        self.list.add_node(20)
        self.list.add_node(30)
        self.list.remove_node(20)
        self.assertEqual(self.list.length_of_list(), 2)
        self.assertEqual(str(self.list), "[10, 30]")

    def test_get_node(self):
        self.list.add_node(10)
        self.list.add_node(20)
        self.list.add_node(30)
        self.assertEqual(self.list.get_node(1).data, 20)

if __name__ == '__main__':
    unittest.main()
