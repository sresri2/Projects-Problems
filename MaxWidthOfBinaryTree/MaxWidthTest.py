# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    def calculateLength(self, listOfNodes):
        leadingNones = 0
        trailingNones = 0
        nodeFound = False
        updatedList = []
        for node in listOfNodes:
            if node:
                nodeFound = True
                for i in range(0,trailingNones):
                    updatedList.append(None)
                trailingNones = 0
                updatedList.append(node)
            else:
                if nodeFound == False:
                    leadingNones += 1
                else:
                    trailingNones += 1
        
        return updatedList
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        orgRoot = root
        listOfNodes = [root]
        MaxWidth = 1
        finalReturn = Solution().traverseTree(listOfNodes,MaxWidth)
        return finalReturn
    def traverseTree(self,listOfNodes,MaxWidth):
        children = []
        for Node in listOfNodes:
            if Node:
                children.append(Node.left)
                children.append(Node.right)
            else:
                children.append(None)
                children.append(None)
        if children != []:
            updatedChildren = Solution().calculateLength(children)
            if len(updatedChildren) > MaxWidth:
                MaxWidth = len(updatedChildren)
            if len(updatedChildren) == 0:s
                return MaxWidth
            MaxWidth = self.traverseTree(updatedChildren, MaxWidth)
        
            
        return MaxWidth
            

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)

print(Solution().widthOfBinaryTree(root))

