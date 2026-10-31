class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=0,len(matrix[0])-1

        while r<len(matrix) and c>=0:
            look=matrix[r][c]
            if look>target: c-=1
            elif look<target: r+=1
            else: return True

        return False