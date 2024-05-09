from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class PreOrderTravesalAlgo:
    def print(self, root, result=[]):
        if not root:
            return result

        result.append(root.value)

        self.print(root.left, result)
        self.print(root.right, result)

        return result


class InOrderTravesalAlgo:
    def print(self, root, result=[]):
        if not root:
            return result
        
        self.print(root.left, result)
        result.append(root.value)
        self.print(root.right, result)

        return result


class PostOrderTravesalAlgo:
    def print(self, root, result=[]):
        if not root:
            return result
        
        self.print(root.left, result)
        self.print(root.right, result)

        result.append(root.value)

        return result



class LevelOrderTraversalAlgo:
    def print(self, root, result=[]):
        if not root:
            return
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return result


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print(self, algo=PreOrderTravesalAlgo()):
        return algo.print(self.root)


bt = BinaryTree(1)
bt.left = Node(2)
bt.right = Node(3)
bt.left.left = Node(4)
bt.left.right = Node(5)
bt.right.left = Node(6)
bt.right.right = Node(7)

