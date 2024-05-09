import unittest
from binary_tree import BinaryTree, Node, PreOrderTravesalAlgo, InOrderTravesalAlgo, PostOrderTravesalAlgo, LevelOrderTraversalAlgo

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree(1)
        self.bt.root.left = Node(2)
        self.bt.root.right = Node(3)
        self.bt.root.left.left = Node(4)
        self.bt.root.left.right = Node(5)
        self.bt.root.right.left = Node(6)
        self.bt.root.right.right = Node(7)

    def test_preorder_traversal(self):
        algo = PreOrderTravesalAlgo()
        expected_output = "1 2 4 5 3 6 7"
        self.assertEqual(' '.join(str(val) for val in self.bt.print(algo=algo)), expected_output)

    def test_inorder_traversal(self):
        algo = InOrderTravesalAlgo()
        expected_output = "4 2 5 1 6 3 7"
        self.assertEqual(' '.join(str(val) for val in self.bt.print(algo=algo)), expected_output)

    def test_postorder_traversal(self):
        algo = PostOrderTravesalAlgo()
        expected_output = "4 5 2 6 7 3 1"
        self.assertEqual(' '.join(str(val) for val in self.bt.print(algo=algo)), expected_output)

    def test_levelorder_traversal(self):
        algo = LevelOrderTraversalAlgo()
        expected_output = "1 2 3 4 5 6 7"
        self.assertEqual(' '.join(str(val) for val in self.bt.print(algo=algo)), expected_output)

if __name__ == '__main__':
    unittest.main()