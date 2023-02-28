# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildNextLevel(self,left,right,root):
        children = [left,right]
        if children[0] == [] and children[1] == []:
            return root
        if children[0]:
            nextLeftRoot =  TreeNode(left[len(left)//2])
        else:
            nextLeftRoot = None
        if children[1]:
            nextRightRoot = TreeNode(right[len(right)//2])
        else:
            nextRightRoot = None

        root.left = nextLeftRoot
        root.right = nextRightRoot

        for childArr in children:
            nextLeft = []
            nextRight = []
            pos = 0
            for Node in childArr:
                if childArr == children[0]:
                    if Node == nextLeftRoot.val:
                        nextRight = childArr[pos + 1:]
                        nextChildren = self.buildNextLevel(nextLeft,nextRight,nextLeftRoot)
                        break
                    else:
                        pos += 1
                        nextLeft.append(Node)

                if childArr == children[1]:
                    if Node == nextRightRoot.val:
                        nextRight = childArr[pos + 1:]
                        nextChildren = self.buildNextLevel(nextLeft,nextRight,nextRightRoot)
                        break
                    else:
                        pos += 1
                        nextLeft.append(Node)
        if not nextChildren:
            return root



        

    def buildTree(self, inorder, postorder):
        if inorder == [] and postorder == []:
            return None
        root = postorder[-1]

        leftSide = []
        rightSide = []
        pos = 0
        for i in inorder:
            if i == root:
                rightSide = inorder[pos+1:]
                break
            else:
                pos += 1
                leftSide.append(i)
        root = TreeNode(root)
        orgRoot = root

        if len(rightSide) > 1 or len(leftSide) > 1:
            tree = self.buildNextLevel(leftSide,rightSide,orgRoot)
        else:
            if leftSide != []:
                root.left = TreeNode(leftSide[0])
            if rightSide != []:
                root.right = TreeNode(rightSide[0])

        return root


print(Solution().buildTree([3,2,1],[3,2,1]))
