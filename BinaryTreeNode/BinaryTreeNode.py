# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        finalList = []
        level = [root]
        finalList = self.traverseTree(level,finalList)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return finalList


    def traverseTree(self, listOfNodes, final):
        children = []
        for Node in listOfNodes:
            if Node.left != None:
                children.append(Node.left)
            if Node.right != None:
                children.append(Node.right)
        if children != []:
            final = self.traverseTree(children, final)

        levelList = []
        for Node in listOfNodes:
            levelList.append(Node.val)
        final.append(levelList)
        return final
        #create list of node values
        #append to overall list
        #return that list

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(20)
root.right.right = TreeNode(25)
root.left.left.right = TreeNode(30)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(18)

print(Solution().levelOrderBottom(root))
        






        