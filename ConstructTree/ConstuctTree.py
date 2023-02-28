# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def partitionTree(self, pivot, inOrder):
        pos = 0
        pivotPos = 0
        for i in inOrder:
            if i == pivot:
                pivotPos = pos
                break
            else:
                pos += 1
        return pivotPos

    def buildTree(self, inorder, postorder):
        if inorder == [] and postorder == []:
            return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        pivotPos = inorder.index(root.val)
        pivotPos = self.partitionTree(root.val, inorder)
        root.left = self.buildTree(inorder[0:pivotPos], postorder[0:pivotPos])
        root.right = self.buildTree(inorder[pivotPos+1:], postorder[pivotPos:-1])

        return root
        

print(Solution().buildTree([11,12,8,4,9,2,10,5,1,6,13,3,7],[12,11,8,9,4,10,5,2,13,6,7,3,1]))

        

        


