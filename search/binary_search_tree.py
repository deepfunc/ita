"""二叉搜索树
"""


def play():
    inorder_tree_walk(1)


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


def inorder_tree_walk(x):
    """中序遍历"""
    if x is not None:
        if not isinstance(x, Node):
            raise Exception('x must be a Node!')

        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


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
