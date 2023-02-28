# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def traverse(self,Node,final):
        if not Node:
            return
        if Node.left:
            self.traverse(Node.left,final)

        final.append(Node.val)
        if Node.right:
            self.traverse(Node.right,final)

        return final
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        final1 = self.traverse(root1,[])
        final2 = self.traverse(root2,[])
        
        final = final1 + final2
        final.sort()
        return final

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
print(Solution().getAllElements(root1,root2))