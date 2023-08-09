import numpy as np
#from line.funcs import *
#from line.params import *
#from params import *

#Triangle vertices
#def tri_vert(a,b,c):
	#return  A,B,C
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
def det(A,B,C):
    #if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        #raise ValueError("Input matrix must be 3x3")

	D = (1* (B[0] * C[1] - C[0] * B[1]) - 1* (A[0] * C[1] - C[0] * A[1]) + 1* (A[0] * B[1] - B[0] * A[1]))
	return D

det_2D1 = (1*B[0]-1*A[0])
det_2D2 = (1*B[1]-1*A[1])
det_2D3 = (1*C[0]-1*B[0])
det_2D4 = (1*C[1]-1*B[1])
det_2D5 = (1*C[0]-1*A[0])
det_2D6 = (1*C[1]-1*A[1])
det_2D7 = (A[0]*B[1]-B[0]*A[1])
det_2D8 = (B[0] * C[1] - C[0] * B[1])
det_2D9 = (A[0] * C[1] - C[0] * A[1])

if det(A,B,C)!=0:
	print("The given points are non-collinear")

elif det_2D1 != 0 or det_2D2 != 0 or det_2D3 != 0 or det_2D4 != 0 or det_2D5 != 0 or det_2D6 != 0 or det_2D7 != 0 or det_2D8 != 0 or det_2D9 != 0:
	print("The given points are collinear")

else:
	print("The given points are non-collinear")
