class TreeNode:
    def __init__(self, value = None, children=None):
        self.value = value
        self.children = list(children) if children else []

class BinaryTreeNode:
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def eulerian_tour(node: TreeNode):
    if node is None:
        return []
    else:
        acc = []
        for child in node.children:
            acc = acc +  eulerian_tour(child)
        return [node.value] + acc + [node.value] 


def inorder_traversal(node: BinaryTreeNode):
    if node is None:
        return []
    else:
        return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

def preorder_traversal(node: BinaryTreeNode):
    if node is None:
        return []
    else:
        return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

def postorder_traversal(node: BinaryTreeNode):
    if node is None:
        return []
    else:
        return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value] 

