#Competitive coding 5:

#problem 1: Greatest value in each row of the tree (https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

#bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q=Queue()
        result = []
        q.put(root)
        while not q.empty():
            qsize = q.qsize()
            maxi = -sys.maxsize - 1
            for i in range(qsize):
                curr = q.get()
                if (curr.val > maxi):
                    maxi = curr.val
                if (curr.left !=None):
                    q.put(curr.left)
                if (curr.right != None):
                    q.put(curr.right)
            result.append(maxi)

        return result

# TC = O(n) ,  SC = O(n) in the worst case when the queue contains nodes from the largest level of the tree.

#dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode] , lvl : int) ->None:
        #base
        if root == None:
            return


        #logic
        if lvl == len(self.result):
            self.result.append(root.val)
        elif self.result[lvl] < root.val:
            self.result[lvl] = root.val

        self.dfs(root.left , lvl + 1)
        self.dfs(root.right , lvl + 1)
#TC = O(n), SC =O(h)

# problem 2:  Valid sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val) 

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
# TC = O(1), SC = O(1)