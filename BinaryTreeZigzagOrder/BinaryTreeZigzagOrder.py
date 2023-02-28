# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getOrderOfNextLevel(self,levelList,direction,final):
        children = []
        if direction == 1:
            for Node in levelList[::-1]:
                if Node:
                    if Node.left:
                        children.append(Node.left)
                    if Node.right:
                        children.append(Node.right)
        if direction == 0:
            for Node in levelList[::-1]:
                if Node:
                    if Node.right:
                        children.append(Node.right)
                    if Node.left:
                        children.append(Node.left)
        if direction == 0:
            direction = 1
        else:
            direction = 0
        if children != []:
            final = self.getOrderOfNextLevel(children,direction,final)
        
        NodeList = []
        for NodeVal in levelList:
            NodeList.append(NodeVal.val)
        final.append(NodeList)
        return final
               
    def zigzagLevelOrder(self, root):
        if not root:
            return None
        
        levelList = [root]
        direction = 0
        finalList = []
        
        finalList = Solution().getOrderOfNextLevel(levelList,direction,finalList)

        return finalList[::-1]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root.left.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)

print(Solution().zigzagLevelOrder(root))
