Matrix = List[List[float]]

A = [[1,2,3],[4,5,6]]
B = [[1,2],[3,4],[5,6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """(열의 개수, 행의개수)를 반환"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3)

def get_row(A: Matrix, i: int) -> Vector:
    '''A의 i번째 행을 반환'''
    return A[i] #A[i]는 i번째 행을 나타낸다.

def get_column(A: Matrix, j: int) -> Vector:
    """A의 j번째 열을 반환"""
    return [[A_i[j]      # A_i 행의 j번째 원소
           for A_i in A] # 각 A_i 행에 대해
            
from typing import Callabel

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callabel[[int, int], float]) -> Matrix:
"""
    (i,j) 번째 원소가 entry_fn(i, j) 인
    num_rows x num_cols 리스트를 반환
"""

return [[entry_fn(i, j)            #i가 주어졌을 때, 리스트를 생성한다.
         for j in range(num_cols)] # [entry_fn(i,0),...]
        for i in range(num_rows)]  # 각 i에 대해 하나의 리스트를 생성한다.

def identity_matrix(n: int) -> Matrix:
    """nxn 단위 행렬을 반환"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
