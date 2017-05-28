For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering requirements:

- The  value of every node in a node's left subtree is less than the data value of that node.
- The  value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

A = []
def makeRootArray(root):
    if root is None:
        return
    global A

    makeRootArray(root.left)
    A.append(root.data)
    makeRootArray(root.right)
    return A
    
def check_binary_search_tree_(root):
        A = makeRootArray(root)
        for x in range(len(A) - 1):
            if A[x] >= A[x + 1]:
                return False
        return True
