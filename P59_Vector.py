from typing import List

Vector = List[float]

height_weight_age = [70,170, 40]

grades = [95,80,75,62]

def add(v: Vector, w:Vector) -> Vector:
    """각 성분끼리 더한다"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1,2,3], [4,5,6]) == [5,7,9]


def subtract(v: Vector, w:Vector) -> Vector:
    """각 성분끼리 뺀다"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert subtract([5,7,9], [4,5,6]) == [1,2,3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """모든 벡터의 각 성분들끼리 더한다,"""
    #vctors가 비어있는지 확인
    assert vectors, "no vectors provided!"
    
    #모든 벡터의 길이가 동일한지 확인
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    
    #i번째 결과값은 모든 벡터의 i성분을 더한값
    return [sum(vector[i] for vector i vectors)
            for i in range(num_elements)]

assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]


def scalar_multiply(c: float, v:Vector) -> Vector:
    """모든 성분을 c로 곱하기."""
    return [ c * v_i for v_i in v]

assert scalar_multiply(2, [1,2,3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """각 성분별 평균을 계산"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]


def dot(v:Vector, w: Vector) -> float:
    """백터의 내적"""
    assert len(v) == len(w), "vectors must be same length"
    
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1, 2, 3], [4, 5 ,6]) == 32 # (1*3) +( 2*5) + (3*6)

def sum_of_squares(v: Vector) -> float:
    '''각 성분의 제곱값의 합 제곱값의 합을 이용하여 벡터의 크기를 구할수있다'''
    return dot(v, v)

assert sum_of_squares([1,2,3]) == 14 #(1*1)+(2*2)+(3*3)


import math

def magnitude(v: Vector) -> float:
    """벡터 v의 크기를 반환"""
    return math.sqrt(sum_of_squares(v)) #제곱근계산

assert sum_of_squares([1,2,3]) == 14    

두 벡터 간의 거리

def squared_distance(v: Vector, w: Vector) -> float:
    """(v_1 -w_1) **2 +...+(v_n -w_n) **2 """
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    """ 벡터 v와 w 간의 거리를 계산"""
    return math.sqrt(squared_distance(v, w))

"""다음과 같이 수정하면 깔끔해진다"""
def distance(v: Vector, w: Vector) ->float:
    return magnitude(subtract(v, w))
