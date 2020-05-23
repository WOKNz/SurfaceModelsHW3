import numpy as np
import matplotlib.pyplot as plt


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return '(X:' + str(self.x) + ' Y:' + str(self.y) + ')'

	@staticmethod
	def npArrayToListOfPoints(points):
		temp_list = []
		for row in range(points.shape[0]):
			temp_list.append(Point(points[row, 0], points[row, 1]))
		return temp_list


class Triangle():
	def __init__(self, p1, p2, p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.triangle_infront_p1 = None
		self.triangle_infront_p2 = None
		self.triangle_infront_p3 = None

	def __str__(self):
		return self.p1.__str__() + self.p2.__str__() + self.p3.__str__()

	def getCornersAsList(self):
		return [self.p1, self.p2, self.p3]

	def getOpositesAsList(self):
		return [self.triangle_infront_p1,
		        self.triangle_infront_p2,
		        self.triangle_infront_p3]

	def getAngle(self, point):
		if point is self.p1:
			a = np.array([self.p2.x, self.p2.y])
			b = np.array([self.p1.x, self.p1.y])
			c = np.array([self.p3.x, self.p3.y])

			ba = a - b
			bc = c - b

			cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
			angle = np.arccos(cosine_angle)

			return angle
		elif point is self.p2:
			a = np.array([self.p1.x, self.p1.y])
			b = np.array([self.p2.x, self.p1.y])
			c = np.array([self.p3.x, self.p3.y])

			ba = a - b
			bc = c - b

			cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
			angle = np.arccos(cosine_angle)

			return angle
		elif point is self.p3:
			a = np.array([self.p1.x, self.p1.y])
			b = np.array([self.p3.x, self.p3.y])
			c = np.array([self.p2.x, self.p2.y])

			ba = a - b
			bc = c - b

			cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
			angle = np.arccos(cosine_angle)

			return angle
		else:
			print('error calculating angle')

	def getOposite(self, point, new_opposite_triangle=None, set_new_opposite_triangle=None):
		if point is None:
			return None
		tot = None  # Opposite triengle
		if self.p1 is point:
			tot = self.triangle_infront_p1
		if self.p2 is point:
			tot = self.triangle_infront_p2
		if self.p3 is point:
			tot = self.triangle_infront_p3
		if tot is None:
			return None
		if tot.p1 is not self.p1 and \
				tot.p1 is not self.p2 and \
				tot.p1 is not self.p3:
			return tot.p1
		if tot.p2 is not self.p1 and \
				tot.p3 is not self.p2 and \
				tot.p3 is not self.p3:
			return tot.p2
		if tot.p3 is not self.p1 and \
				tot.p3 is not self.p2 and \
				tot.p3 is not self.p3:
			return tot.p3

	def inCircle(self, point):
		opposite = self.getOposite(point)
		if opposite is None:
			return False
		temp_mat = np.array([[self.p1.x, self.p1.y, self.p1.x ** 2, self.p1.y ** 2],
		                     [self.p2.x, self.p2.y, self.p2.x ** 2, self.p2.y ** 2],
		                     [self.p3.x, self.p3.y, self.p3.x ** 2, self.p3.y ** 2],
		                     [opposite.x, opposite.y, opposite.x ** 2, opposite.y ** 2]])
		if np.linalg.det(temp_mat) >= 0:
			return True
		else:
			return False

	@staticmethod
	def updateTriangle(triangle, triangle_to_update, new_triangle):
		if triangle.triangle_infront_p1 is triangle_to_update:
			triangle.triangle_infront_p1 = new_triangle
		elif triangle.triangle_infront_p2 is triangle_to_update:
			triangle.triangle_infront_p2 = new_triangle
		elif triangle.triangle_infront_p3 is triangle_to_update:
			triangle.triangle_infront_p3 = new_triangle
		else:
			print('no triangle to update')

	#
	# def updateCorner(self, corner_to_update, new_corner):
	#
	# 	if self.p1 is corner_to_update:
	# 		self.p1 = new_corner
	# 	elif self.p2 is corner_to_update:
	# 		self.p2 = new_corner
	# 	elif self.p3 is corner_to_update:
	# 		self.p3 = new_corner
	# 	else:
	# 		print('no corner to update')
	def oppositCorner(self, point):
		if self.p1 is point:
			if self.triangle_infront_p1 is not None:
				if self.triangle_infront_p1.p1 is not self.p2 and self.triangle_infront_p1.p1 is not self.p3:
					return self.triangle_infront_p1.p1
				if self.triangle_infront_p1.p2 is not self.p2 and self.triangle_infront_p1.p2 is not self.p3:
					return self.triangle_infront_p1.p2
				if self.triangle_infront_p1.p3 is not self.p2 and self.triangle_infront_p1.p3 is not self.p3:
					return self.triangle_infront_p1.p3
			else:
				return None
		if self.p2 is point:
			if self.triangle_infront_p2 is not None:
				if self.triangle_infront_p2.p1 is not self.p1 and self.triangle_infront_p2.p1 is not self.p3:
					return self.triangle_infront_p2.p1
				if self.triangle_infront_p2.p2 is not self.p1 and self.triangle_infront_p2.p2 is not self.p3:
					return self.triangle_infront_p2.p2
				if self.triangle_infront_p2.p3 is not self.p1 and self.triangle_infront_p2.p3 is not self.p3:
					return self.triangle_infront_p2.p3
			else:
				return None
		if self.p3 is point:
			if self.triangle_infront_p3 is not None:
				if self.triangle_infront_p3.p1 is not self.p2 and self.triangle_infront_p3.p1 is not self.p1:
					return self.triangle_infront_p3.p1
				if self.triangle_infront_p3.p2 is not self.p2 and self.triangle_infront_p3.p2 is not self.p1:
					return self.triangle_infront_p3.p2
				if self.triangle_infront_p3.p3 is not self.p2 and self.triangle_infront_p3.p3 is not self.p1:
					return self.triangle_infront_p3.p3
			else:
				return None

	def opositeTriange(self, point):
		if self.p1 is point:
			return self.triangle_infront_p1
		if self.p2 is point:
			return self.triangle_infront_p2
		if self.p3 is point:
			return self.triangle_infront_p3

	def flip(self, other_triangle):

		if other_triangle is None:
			return 0
		N = self
		O = other_triangle

		# Make p1 to be point A (close point) (self triangle)
		if N.p2 is not O.p1 and \
				N.p2 is not O.p2 and \
				N.p2 is not O.p3:
			N.p1, N.p2 = N.p2, N.p1
			N.triangle_infront_p1, N.triangle_infront_p2 = N.triangle_infront_p2, \
			                                               N.triangle_infront_p1
		elif N.p3 is not O.p1 and \
				N.p3 is not O.p2 and \
				N.p3 is not O.p3:
			N.p1, N.p3 = N.p3, N.p1
			N.triangle_infront_p1, N.triangle_infront_p3 = N.triangle_infront_p3, \
			                                               N.triangle_infront_p1

		# Make p3 to be point B (far point) (other triangle)
		if O.p2 is not N.p1 and \
				O.p2 is not N.p2 and \
				O.p2 is not N.p3:
			O.p3, O.p2 = O.p2, O.p3
			O.triangle_infront_p3, O.triangle_infront_p2 = O.triangle_infront_p2, \
			                                               O.triangle_infront_p3
		elif O.p1 is not N.p1 and \
				O.p1 is not N.p2 and \
				O.p1 is not N.p3:
			O.p3, O.p1 = O.p1, O.p3
			O.triangle_infront_p3, O.triangle_infront_p1 = O.triangle_infront_p1, \
			                                               O.triangle_infront_p3

		# Make N.p2 to be other.p1
		if N.p2 is not O.p1:
			O.p1, O.p2 = O.p2, O.p1
			O.triangle_infront_p1, O.triangle_infront_p2 = O.triangle_infront_p2, \
			                                               O.triangle_infront_p1

		A = N.triangle_infront_p3
		B = O.triangle_infront_p2
		C = N.triangle_infront_p2
		D = O.triangle_infront_p1
		N.triangle_infront_p2 = O
		N.triangle_infront_p1 = B
		O.triangle_infront_p2 = N
		O.triangle_infront_p3 = C
		if B is not None:
			self.updateTriangle(B, O, N)
		if C is not None:
			self.updateTriangle(C, N, O)
		N.p3 = O.p3
		O.p1 = N.p1
		return 1


class DelaunoyTriangulation():
	def __init__(self, points):
		self.j = 0
		self.points = points
		self.points_obj_list = Point.npArrayToListOfPoints(points)
		self.triangles = None
		# Bounding box dimensionsz
		width = np.max(points[:, 0]) - np.min(points[:, 0])
		higth = np.max(points[:, 1]) - np.min(points[:, 1])
		M = max((width, higth))

		# Center of Mass (points)
		x_c = np.average(points[:, 0])
		y_c = np.average(points[:, 1])

		# Corners of covering triangle
		self.p1 = Point(x_c + 3 * M, y_c)
		self.p2 = Point(x_c, y_c + 3 * M)
		self.p3 = Point(x_c - 3 * M, y_c - 3 * M)
		# self.p1 = Point(120,0)
		# self.p2 = Point(0,120)
		# self.p3 = Point(-120,-120)
		self.triangles = [Triangle(self.p1, self.p2, self.p3)]

		# plt.scatter(points[:,0], points[:,1], color='blue')
		# plt.scatter([self.p1.x,self.p2.x,self.p3.x],
		#             [self.p1.y,self.p2.y,self.p3.y], color='red')
		# plt.show()

		for point in self.points_obj_list:
			# self.plotDiagramm()
			self.split(point, self.inWhichTriangle(point))
		# # self.plotDiagramm()
		# self.checkFlip(self.triangles[-1],self.triangles[-1].oppositCorner(point))
		# # self.plotDiagramm()
		# self.checkFlip(self.triangles[-2],self.triangles[-2].oppositCorner(point))
		# # self.plotDiagramm()
		# self.checkFlip(self.triangles[-3],self.triangles[-3].oppositCorner(point))
		# # self.plotDiagramm()

		stop = 1
		while stop > 0:
			stop = 0
			for triangle in self.triangles:
				stop = stop + self.checkFlip(triangle, triangle.p1)
				stop = stop + self.checkFlip(triangle, triangle.p2)
				stop = stop + self.checkFlip(triangle, triangle.p3)

		self.plotDiagramm('beforeclean')

		max_len = len(self.triangles)
		triangles_to_keep = []

		for i in range(0, max_len):
			if self.p1 is self.triangles[i].p1 or \
					self.p1 is self.triangles[i].p2 or \
					self.p1 is self.triangles[i].p3 or \
					self.p2 is self.triangles[i].p1 or \
					self.p2 is self.triangles[i].p2 or \
					self.p2 is self.triangles[i].p3 or \
					self.p3 is self.triangles[i].p1 or \
					self.p3 is self.triangles[i].p2 or \
					self.p3 is self.triangles[i].p3:
				continue
			else:
				if len(self.triangles) > 0:
					triangles_to_keep.append(self.triangles[i])
		self.triangles = triangles_to_keep
		self.plotDiagramm('afterclean')

	def isInsideTriangle(self, point, triangle):
		Dx, Dy = point.x, point.y
		Ax, Ay = triangle.p1.x, triangle.p1.y
		Bx, By = triangle.p2.x, triangle.p2.y
		Cx, Cy = triangle.p3.x, triangle.p3.y

		M1 = np.array([[Dx - Bx, Dy - By, 0],
		               [Ax - Bx, Ay - By, 0],
		               [1, 1, 1]
		               ])

		M2 = np.array([[Dx - Ax, Dy - Ay, 0],
		               [Cx - Ax, Cy - Ay, 0],
		               [1, 1, 1]
		               ])

		M3 = np.array([[Dx - Cx, Dy - Cy, 0],
		               [Bx - Cx, By - Cy, 0],
		               [1, 1, 1]
		               ])

		M1 = np.linalg.det(M1)
		M2 = np.linalg.det(M2)
		M3 = np.linalg.det(M3)

		if (M1 == 0 or M2 == 0 or M3 == 0):
			print("Point: ", point, " lies on the arms of Triangle")
			return True
		elif ((M1 > 0 and M2 > 0 and M3 > 0) or (M1 < 0 and M2 < 0 and M3 < 0)):
			return True
		else:
			return False

	def inWhichTriangle(self, point):
		for triangle in self.triangles:
			if self.isInsideTriangle(point, triangle):
				return triangle

	def checkFlip(self, new_triangle, point):
		if point is None or new_triangle is None:
			return 0
		if new_triangle.inCircle(point):
			return new_triangle.flip(new_triangle.opositeTriange(point))
		return 0

	def split(self, pointA, triangle):
		temp_trianle1A2 = Triangle(triangle.p1, pointA, triangle.p2)
		temp_trianle2A3 = Triangle(triangle.p2, pointA, triangle.p3)
		temp_trianle3A1 = Triangle(triangle.p3, pointA, triangle.p1)

		temp_trianle1A2.triangle_infront_p1 = temp_trianle2A3
		temp_trianle1A2.triangle_infront_p3 = temp_trianle3A1
		temp_trianle2A3.triangle_infront_p1 = temp_trianle3A1
		temp_trianle2A3.triangle_infront_p3 = temp_trianle1A2
		temp_trianle3A1.triangle_infront_p1 = temp_trianle1A2
		temp_trianle3A1.triangle_infront_p3 = temp_trianle2A3

		temp_trianle1A2.triangle_infront_p2 = triangle.triangle_infront_p3
		temp_trianle2A3.triangle_infront_p2 = triangle.triangle_infront_p1
		temp_trianle3A1.triangle_infront_p2 = triangle.triangle_infront_p2

		self.triangles.extend([temp_trianle1A2, temp_trianle2A3, temp_trianle3A1])
		self.triangles.remove(triangle)

	def plotDiagramm(self, Name=None):
		fig = plt.figure()
		for triangle in self.triangles:
			plt.plot([triangle.p1.x, triangle.p2.x, triangle.p3.x, triangle.p1.x],
			         [triangle.p1.y, triangle.p2.y, triangle.p3.y, triangle.p1.y], linewidth=0.25)
		plt.scatter(self.points[:, 0], self.points[:, 1], color='red', s=2.0)
		if Name is not None:
			plt.savefig(Name, dpi=600)
		fig.show()
