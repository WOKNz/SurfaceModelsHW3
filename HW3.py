import numpy as np
import pandas as pd
from delanoy import DelaunoyTriangulation as dt
from delanoy2 import Point, Triangle, DelaunoyTriangulation

if __name__ == "__main__":
	# points_np = np.genfromtxt('data/data3.xyz')  # (X,Y,Z)
	# # print(pd.DataFrame(points))
	# # for row in range(points_np.shape[0]):
	#
	# triangulation = dt(points_np)

	# Testing unit for internal functions
	#    Creating data
	#        Creating Points
	p1 = Point(-3.3, 5.9, 'P1')
	p2 = Point(0, 5, 'P2')
	p3 = Point(3.1, 6, 'P3')
	p4 = Point(-0.4, 2.1, 'P4')
	p5 = Point(0, 0, 'P5')
	p6 = Point(2, 2, 'P6')
	p7 = Point(-3, -1, 'P7')
	p8 = Point(3, -2, 'P8')

	#        Creating Triangles
	tri1 = Triangle(p1, p2, p4, id='T1')
	tri2 = Triangle(p2, p3, p6, id='T2')
	tri3 = Triangle(p4, p2, p5, id='T3')
	tri4 = Triangle(p2, p6, p5, id='T4')
	tri5 = Triangle(p4, p7, p5, id='T5')
	tri6 = Triangle(p5, p6, p8, id='T6')

	#        Creating Triangles Corner Opposites
	tri1.tri_p1, tri1.tri_p2, tri1.tri_p3 = tri3, None, None
	tri2.tri_p1, tri2.tri_p2, tri2.tri_p3 = None, tri4, None
	tri3.tri_p1, tri3.tri_p2, tri3.tri_p3 = tri4, tri5, tri1
	tri4.tri_p1, tri4.tri_p2, tri4.tri_p3 = tri6, tri3, tri2
	tri5.tri_p1, tri5.tri_p2, tri5.tri_p3 = None, tri3, None
	tri6.tri_p1, tri6.tri_p2, tri6.tri_p3 = None, None, tri4

	# Graph befoer manipulating
	delaunoy1 = DelaunoyTriangulation(None)
	delaunoy1.points = [p1, p2, p3, p4, p5, p6, p7, p8]
	delaunoy1.triangles = [tri1, tri2, tri3, tri4, tri5, tri6]
	delaunoy1.plotDiagramm(unpad=0.1)

	#    Testing Match Function
	tri4.match(p2)
	#    Testing Flip Function

	tri3.flip(p4)

	# Graph after manipulating
	delaunoy2 = DelaunoyTriangulation(None)
	delaunoy2.points = [p1, p2, p3, p4, p5, p6, p7, p8]
	delaunoy2.triangles = [tri1, tri2, tri3, tri4, tri5, tri6]
	delaunoy2.plotDiagramm(unpad=0.1)
