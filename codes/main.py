import numpy as np

np.set_printoptions(precision=2)


a1 = 1
a2 = -1
b1 = -4
b2 = 6
c1 = -3
c2 = -5

A= np.array([a1,a2])
B= np.array([b1,b2])
C= np.array([c1,c2])

Mat = np.array([[1,1,1],[a1,b1,c1],[a2,b2,c2]])

rank = np.linalg.matrix_rank(Mat)

if (rank==2):
	print("The points A,B,C are collinear")
else:
	print("The points A,B,C are not collinear")
