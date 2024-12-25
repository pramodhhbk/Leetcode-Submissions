class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        low = 0
        high = (r*c) - 1
        while(low<=high):
            mid = (low+high)//2
            row = mid//c
            col = mid%c
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]<target):
                low+=1
            else:
                high-=1
        
        return False