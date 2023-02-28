# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def find(self,search,root,seq):
        if seq:
            if root.val > search:
                return 0
            else:
                left = self.find(root.left,search - root.val,True)
                right = self.find(root.right,search-root.val,True)
                return left + right
        else:
            if root.val > search:
                left = find(root.left,search,False)
                right = find(root.right,search,False)

                return left + right
            else:
                leftSeq = self.find(root.left,search - root.val,True)
                rightSeq = self.find(root.right,search-root.val,True)

                left = self.find(root.left,search,False)
                right = self.find(root.right,search,False)

                return left + right + leftSeq + rightSeq


    def traverse(self, root, sum):
        if root == None:
            return [],[]
        lLists, alList = self.traverse(root.left, sum)
        rLists, arlist = self.traverse(root.right, sum)
        retList = lLists + rLists
        

        addableList = alList + arlist
        pos = 0
        for i in addableList:
            addableList[pos]+=root.val
            pos+=1
        addableList.append(root.val)

        
        return retList+addableList, addableList
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        list, addableList = self.traverse(root,sum)
    
        return list.count(sum)
        
        
        
        


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)

root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)

print(Solution().pathSum(root,8))