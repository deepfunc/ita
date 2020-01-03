from .binary_search_tree import \
    Node, tree_search, iterative_tree_search, \
    inorder_tree_walk, preorder_tree_walk, postorder_tree_walk, \
    tree_minimum, tree_maximum


class TestBinarySearchTree(object):
    def test_tree_walk(self):
        root = Node(6)
        root.set_left_node(
            Node(5, left_node=Node(2), right_node=Node(5))
        )
        root.set_right_node(
            Node(7, right_node=Node(8))
        )

        nodes = []

        def handler(node):
            nodes.append(node.key)

        inorder_tree_walk(root, handler)
        assert nodes == [2, 5, 5, 6, 7, 8]

        nodes.clear()
        preorder_tree_walk(root, handler)
        assert nodes == [6, 5, 2, 5, 7, 8]

        nodes.clear()
        postorder_tree_walk(root, handler)
        assert nodes == [2, 5, 5, 8, 7, 6]

    def test_search(self):
        root = Node(6)
        root.set_left_node(
            Node(5, left_node=Node(2), right_node=Node(5))
        )
        root.set_right_node(
            Node(7, right_node=Node(8))
        )

        x = tree_search(root, 5)
        assert x is not None
        assert x.p == root
        assert x.left.key == 2

        x = tree_search(root, 66)
        assert x is None

        x = iterative_tree_search(root, 7)
        assert x is not None
        assert x.p.key == 6
        assert x.right.key == 8

    def test_min(self):
        root = Node(6)
        root.set_left_node(
            Node(5, left_node=Node(2), right_node=Node(5))
        )
        root.set_right_node(
            Node(7, right_node=Node(8))
        )

        assert tree_minimum(root).key == 2
        assert tree_maximum(root).key == 8
