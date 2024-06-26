class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class BSTMapNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += str(self.left)
        ret_str += "{" + str(self.key) + ":" + str(self.data) + "} "
        if self.right != None:
            ret_str += str(self.right)
        return ret_str

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, key, data, node):
        if node == None:
            self.size += 1
            return BSTMapNode(key, data)
        elif key < node.key:
            node.left = self._add(key, data, node.left)
        elif node.key < key:
            node.right = self._add(key, data, node.right)
        else:
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        self.root = self._add(key, data, self.root)

    def _find_node(self, key):
        node = self.root
        while node != None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def update(self, key, data):
        node = self._find_node(key)
        if node == None:
            raise NotFoundException()
        node.data = data

    def find(self, key):
        node = self._find_node(key)
        if node == None:
            raise NotFoundException()
        return node.data

    def contains(self, key):
        return self._find_node(key) != None

    def _swap_and_remove_leftmost(self, org_node, node):
        if node.left == None:
            org_node.key = node.key
            org_node.data = node.data
            return self._remove_node(node)
        else:
            node.left = self._swap_and_remove_leftmost(org_node, node.left)
            return node

    def _remove_node(self, node):
        if node.left == None and node.right == None:
            return None
        elif node.right == None:
            return node.left
        elif node.left == None:
            return node.right
        else:
            node.right = self._swap_and_remove_leftmost(node, node.right)
            return node

    def _remove(self, key, node):
        if node == None:
            raise NotFoundException()
        if key < node.key:
            node.left = self._remove(key, node.left)
        elif node.key < key:
            node.right = self._remove(key, node.right)
        else:
            self.size -= 1
            return self._remove_node(node)
        return node

    def remove(self, key):
        self.root = self._remove(key, self.root)

    def __str__(self):
        return str(self.root).strip() if self.root != None else ""

    def __len__(self):
        return self.size
