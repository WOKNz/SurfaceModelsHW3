import numpy as np
import pandas as pd
from delanoy import DelaunoyTriangulation as dt
from delanoy2 import DelaunoyTriangulation

if __name__ == "__main__":
	points_np = np.genfromtxt('data/data.xyz')  # (X,Y,Z)
	delaunoy3 = DelaunoyTriangulation(points_np)
	delaunoy3.plotDiagramm(unpad=0.1, Name='data_triangulated_delunoy.png')
