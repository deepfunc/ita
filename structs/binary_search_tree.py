"""二叉搜索树
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        self_str = 'Node(key={}, p.key={}, left.key={}, right.key={})'
        p_key = None if self.p is None else self.p.key
        l_key = None if self.left is None else self.left.key
        r_key = None if self.right is None else self.right.key
        return self_str.format(self.key, p_key, l_key, r_key)

    __repr__ = __str__

    def set_left_node(self, node):
        self.left = node

    def set_right_node(self, node):
        self.right = node


def preorder_tree_walk(node, handler):
    """先序遍历"""
    if node is not None:
        handler(node)
        inorder_tree_walk(node.left, handler)
        inorder_tree_walk(node.right, handler)


def inorder_tree_walk(node, handler):
    """中序遍历"""
    if node is not None:
        inorder_tree_walk(node.left, handler)
        handler(node)
        inorder_tree_walk(node.right, handler)


def postorder_tree_walk(node, handler):
    """后序遍历"""
    if node is not None:
        inorder_tree_walk(node.left, handler)
        inorder_tree_walk(node.right, handler)
        handler(node)


def tree_search(x, key):
    """递归查找"""
    if x is None or x.key == key:
        return x
    if key < x.key:
        return tree_search(x.left, key)
    else:
        return tree_search(x.right, key)


def iterative_tree_search(x, key):
    """迭代查找"""
    while x is not None and x.key != key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x
