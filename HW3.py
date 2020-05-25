import numpy as np
import pandas as pd
from delanoy import DelaunoyTriangulation as dt
from delanoy import DelaunoyTriangulation

if __name__ == "__main__":
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
