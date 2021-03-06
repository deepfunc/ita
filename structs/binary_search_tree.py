"""二叉搜索树
"""


class Node:
    def __init__(self, key, left_node=None, right_node=None):
        self.key = key
        self.p = None
        self.left = left_node
        if self.left is not None:
            self.left.p = self
        self.right = right_node
        if self.right is not None:
            self.right.p = self

    def __str__(self):
        self_str = 'Node(key={}, p.key={}, left.key={}, right.key={})'
        p_key = None if self.p is None else self.p.key
        l_key = None if self.left is None else self.left.key
        r_key = None if self.right is None else self.right.key
        return self_str.format(self.key, p_key, l_key, r_key)

    __repr__ = __str__

    def set_left_node(self, node):
        self.left = node
        node.p = self

    def set_right_node(self, node):
        self.right = node
        node.p = self


class BinarySearchTree:
    def __init__(self):
        self.root = None


def preorder_tree_walk(node, handler):
    """先序遍历"""
    if node is not None:
        handler(node)
        preorder_tree_walk(node.left, handler)
        preorder_tree_walk(node.right, handler)


def inorder_tree_walk(node, handler):
    """中序遍历"""
    if node is not None:
        inorder_tree_walk(node.left, handler)
        handler(node)
        inorder_tree_walk(node.right, handler)


def postorder_tree_walk(node, handler):
    """后序遍历"""
    if node is not None:
        postorder_tree_walk(node.left, handler)
        postorder_tree_walk(node.right, handler)
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


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    """中序遍历中寻找后继"""
    if x.right is not None:
        return tree_minimum(x.right)

    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p

    return y


def tree_predecessor(x):
    """中序遍历中寻找前驱"""
    if x.left is not None:
        return tree_maximum(x.left)

    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p

    return y


def tree_insert(tree, z):
    y = None
    x = tree.root

    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right

    z.p = y
    if y is None:
        tree.root = z
    elif z.key < x.key:
        y.left = z
    else:
        y.right = z


def transplant(tree, u, v):
    """用以 v 为根的子树替换一棵以 u 为根的子树"""
    if u.p is None:
        tree.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p
