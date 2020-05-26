import numpy as np
import pandas as pd
from scipy.spatial import Delaunay
from delanoy import DelaunoyTriangulation
from time import time

if __name__ == "__main__":
	# HW3
	points_np = np.genfromtxt('data/data.xyz')  # (X,Y,Z)
	# points_np = np.random.randn(5,2)
	# np.savetxt('last_random_test2.xyz',points_np)
	delaunoy3 = DelaunoyTriangulation(points_np)
	# delaunoy3.plotDiagramm(Name='data_triangulated_delunoy.png')
	delaunoy3.plotDiagramm('testset4_my.png')

	from scipy.spatial import Delaunay
	import matplotlib.pyplot as plt

	# points_np = points_np[[183,176,163,156,143,137,123,102,95,116,136,144,155],:]
	tri = Delaunay(points_np[:, 0:2])
	plt.triplot(points_np[:, 0], points_np[:, 1], tri.simplices, linewidth=0.25)
	plt.plot(points_np[:, 0], points_np[:, 1], 'o', markersize=0.2)
	plt.savefig('testset4_sci.png', dpi=600)
	plt.show()

# # speed tests
# list_speeds = [] # Delanoy,Scipy
# tests = [*range(50,1000,50)]
# for test in tests:
# 	temp_result_delanoy = None
# 	temp_result_scipy = None
# 	points_np = np.random.randn(test, 2)
#
# 	time1 = time()
# 	delaunoy3 = DelaunoyTriangulation(points_np)
#
# 	time2 = time()
#
# 	tri = Delaunay(points_np[:, 0:2])
# 	time3 = time()
#
# 	temp_result_delanoy = time2-time1
# 	temp_result_scipy = time3- time2
#
# 	list_speeds.append([temp_result_delanoy,temp_result_scipy])
#
# num_points_np = np.array(tests).reshape(len(list_speeds),1)
# results_speed = pd.DataFrame(np.hstack((num_points_np,np.array(list_speeds))))
# results_speed.columns = ['Number of points','Delanoy.py','Scipy']
# results_speed.to_csv('speed_results.csv', index=False)
