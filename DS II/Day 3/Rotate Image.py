class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lb = 0
        ub = len(matrix) - 1
        while(lb < ub):
            for i in range(ub - lb):
                self.swap(matrix, (lb, i + lb), (ub - i, lb))
                self.swap(matrix, (ub - i, lb), (ub, ub - i))
                self.swap(matrix, (ub, ub - i), (i + lb, ub))
            ub -= 1
            lb += 1
            
    def swap(self, matrix, coords1, coords2):
        temp = matrix[coords1[0]][coords1[1]]
        matrix[coords1[0]][coords1[1]] = matrix[coords2[0]][coords2[1]]
        matrix[coords2[0]][coords2[1]] = temp
