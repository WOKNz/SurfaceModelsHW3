import numpy as np
import matplotlib.pyplot as plt
import copy


class Point():
	def __init__(self, x, y, id=None):
		self.x = x
		self.y = y
		self.id = id

	def __str__(self):
		if self.id is None:
			return '(' + str(self.x) + ',' + str(self.y) + ')'
		else:
			return str(self.id) + ' (' + str(self.x) + ',' + str(self.y) + ')'


class Triangle():
	def __init__(self, p1, p2, p3, tri_p1=None, tri_p2=None, tri_p3=None, id=None):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.tri_p1 = tri_p1
		self.tri_p2 = tri_p2
		self.tri_p3 = tri_p3
		self.id = id

	def __str__(self):
		if self.id is None:
			return self.p1.__str__() + ',' + self.p2.__str__() + ',' + self.p3.__str__()
		else:
			return str(self.id) + ' (' + self.p1.id + ',' + self.p2.id + ',' + self.p3.id + ']'

	def match(self, point):

		def oposite(self):
			ot = self.tri_p1  # Opposite Triangle
			if ot.p1 is not self.p2 and ot.p1 is not self.p3:
				return ot.p1
			if ot.p2 is not self.p2 and ot.p2 is not self.p3:
				return ot.p2
			if ot.p3 is not self.p2 and ot.p2 is not self.p3:
				return ot.p3

		# Set p1 in self to be interest point
		if point is self.p2:
			self.p1, self.p2 = self.p2, self.p1
			self.tri_p1, self.tri_p2 = self.tri_p2, self.tri_p1
		if point is self.p3:
			self.p1, self.p3 = self.p3, self.p1
			self.tri_p1, self.tri_p3 = self.tri_p3, self.tri_p1

		op = oposite(self)  # Opposite point

		# Set p1 in other to be interest point
		if op is self.tri_p1.p2:
			self.tri_p1.p1, self.tri_p1.p2 = self.tri_p1.p2, self.tri_p1.p1
			self.tri_p1.tri_p1, self.tri_p1.tri_p2 = self.tri_p1.tri_p2, self.tri_p1.tri_p1
		if op is self.tri_p1.p3:
			self.tri_p1.p1, self.tri_p1.p3 = self.tri_p1.p3, self.tri_p1.p1
			self.tri_p1.tri_p1, self.tri_p1.tri_p3 = self.tri_p1.tri_p3, self.tri_p1.tri_p1

		# Matching other two points
		if self.p2 is self.tri_p1.p3:
			self.tri_p1.p2, self.tri_p1.p3 = self.tri_p1.p3, self.tri_p1.p2
			self.tri_p1.tri_p2, self.tri_p1.tri_p3 = self.tri_p1.tri_p3, self.tri_p1.tri_p2

	def flip(self, point):

		def updateInFrontOfInfrontTriangle(self, point_str, triangle_to_set):
			if point_str == 'p1':
				if self.tri_p1 is None:
					return
				if self.tri_p1.p1 is not self.p2 and \
						self.tri_p1.p1 is not self.p3:
					self.tri_p1.tri_p1 = triangle_to_set
				elif self.tri_p1.p2 is not self.p2 and \
						self.tri_p1.p2 is not self.p3:
					self.tri_p1.tri_p2 = triangle_to_set
				elif self.tri_p1.p3 is not self.p2 and \
						self.tri_p1.p3 is not self.p3:
					self.tri_p1.tri_p3 = triangle_to_set
				else:
					print('Failed to update infront of infront triangle')
			if point_str == 'p2':
				if self.tri_p2 is None:
					return
				if self.tri_p2.p1 is not self.p1 and \
						self.tri_p2.p1 is not self.p3:
					self.tri_p2.tri_p1 = triangle_to_set
				elif self.tri_p2.p2 is not self.p1 and \
						self.tri_p2.p2 is not self.p3:
					self.tri_p2.tri_p2 = triangle_to_set
				elif self.tri_p2.p3 is not self.p1 and \
						self.tri_p2.p3 is not self.p3:
					self.tri_p2.tri_p3 = triangle_to_set
				else:
					print('Failed to update infront of infront triangle')
			if point_str == 'p3':
				if self.tri_p3 is None:
					return
				if self.tri_p3.p1 is not self.p2 and \
						self.tri_p3.p1 is not self.p1:
					self.tri_p3.tri_p1 = triangle_to_set
				elif self.tri_p3.p2 is not self.p2 and \
						self.tri_p3.p2 is not self.p1:
					self.tri_p3.tri_p2 = triangle_to_set
				elif self.tri_p3.p3 is not self.p2 and \
						self.tri_p3.p3 is not self.p1:
					self.tri_p3.tri_p3 = triangle_to_set
				else:
					print('Failed to update infront of infront triangle')

		self.match(point)

		thisTri = self
		otherTri = self.tri_p1

		# Updating outer triangles

		updateInFrontOfInfrontTriangle(thisTri, 'p2', otherTri)
		updateInFrontOfInfrontTriangle(otherTri, 'p3', thisTri)

		a = thisTri.tri_p3
		b = otherTri.tri_p3
		c = thisTri.tri_p2
		d = otherTri.tri_p2

		thisTri.tri_p1 = b
		thisTri.tri_p2 = otherTri
		otherTri.tri_p1 = c
		otherTri.tri_p3 = thisTri

		thisTri.p3 = otherTri.p1
		otherTri.p2 = thisTri.p1

	def isInCircle(self, point):

		def oposite(self):  # Repeated code, make sure you use after match()
			ot = self.tri_p1  # Opposite Triangle
			if ot.p1 is not self.p2 and ot.p1 is not self.p3:
				return ot.p1
			if ot.p2 is not self.p2 and ot.p2 is not self.p3:
				return ot.p2
			if ot.p3 is not self.p2 and ot.p2 is not self.p3:
				return ot.p3

		op = oposite(self)

		if op is None:
			return False

		def ccw(self):
			temp_mat = np.array([[self.p2.x, self.p2.y, 1],
			                     [self.p1.x, self.p1.y, 1],
			                     [self.p3.x, self.p3.y, 1]])
			det = np.linalg.det(temp_mat)
			if det > 0:
				return True
			elif det == 0:
				print('The ', self.__str__(), ' have no area, all points on same line')
				return True
			else:
				return False

		temp_mat = None
		if ccw(self):
			temp_mat = np.array([[self.p2.x, self.p2.y, self.p2.x ** 2 + self.p2.y ** 2, 1],
			                     [self.p1.x, self.p1.y, self.p1.x ** 2 + self.p1.y ** 2, 1],
			                     [self.p3.x, self.p3.y, self.p3.x ** 2 + self.p3.y ** 2, 1],
			                     [op.x, op.y, op.x ** 2 + op.y ** 2, 1]])
		else:
			temp_mat = np.array([[self.p3.x, self.p3.y, self.p3.x ** 2 + self.p3.y ** 2, 1],
			                     [self.p1.x, self.p1.y, self.p1.x ** 2 + self.p1.y ** 2, 1],
			                     [self.p2.x, self.p2.y, self.p2.x ** 2 + self.p2.y ** 2, 1],
			                     [op.x, op.y, op.x ** 2 + op.y ** 2, 1]])

		if np.linalg.det(temp_mat) > 0:
			return True
		else:
			return False

	def isFlip(self, point):
		self.match(point)
		if self.isInCircle(point):
			self.flip(point)

class DelaunoyTriangulation():
	def __init__(self, points):
		self.j = 0
		self.points = points
		# self.points_obj_list = Point.npArrayToListOfPoints(points)
		self.triangles = None

	# # Bounding box dimensionsz
	# width = np.max(points[:, 0]) - np.min(points[:, 0])
	# higth = np.max(points[:, 1]) - np.min(points[:, 1])
	# M = max((width, higth))
	#
	# # Center of Mass (points)
	# x_c = np.average(points[:, 0])
	# y_c = np.average(points[:, 1])
	#
	# # Corners of covering triangle
	# self.p1 = Point(x_c + 3 * M, y_c)
	# self.p2 = Point(x_c, y_c + 3 * M)
	# self.p3 = Point(x_c - 3 * M, y_c - 3 * M)

	def plotDiagramm(self, Name=None, unpad=None):
		fig = plt.figure()

		def addRadilBias(triangle, unpad):
			tt = copy.deepcopy(triangle)  # temp triangle
			x_avg = (tt.p1.x + tt.p2.x + tt.p3.x) / 3.0
			y_avg = (tt.p1.y + tt.p2.y + tt.p3.y) / 3.0
			p1_radial_angle = np.arctan2(y_avg - tt.p1.y, x_avg - tt.p1.x)
			p2_radial_angle = np.arctan2(y_avg - tt.p2.y, x_avg - tt.p2.x)
			p3_radial_angle = np.arctan2(y_avg - tt.p3.y, x_avg - tt.p3.x)
			tt.p1.x = tt.p1.x + np.cos(p1_radial_angle) * unpad
			tt.p1.y = tt.p1.y + np.sin(p1_radial_angle) * unpad
			tt.p2.x = tt.p2.x + np.cos(p2_radial_angle) * unpad
			tt.p2.y = tt.p2.y + np.sin(p2_radial_angle) * unpad
			tt.p3.x = tt.p3.x + np.cos(p3_radial_angle) * unpad
			tt.p3.y = tt.p3.y + np.sin(p3_radial_angle) * unpad
			return (x_avg, y_avg), tt

		if unpad is not None:
			for triangle in self.triangles:
				center, temp_tri = addRadilBias(triangle, unpad)
				plt.plot([temp_tri.p1.x, temp_tri.p2.x, temp_tri.p3.x, temp_tri.p1.x],
				         [temp_tri.p1.y, temp_tri.p2.y, temp_tri.p3.y, temp_tri.p1.y], linewidth=0.25)
				plt.text(center[0], center[1], triangle.id, fontsize=8)
		else:
			for triangle in self.triangles:
				plt.plot([triangle.p1.x, triangle.p2.x, triangle.p3.x, triangle.p1.x],
				         [triangle.p1.y, triangle.p2.y, triangle.p3.y, triangle.p1.y], linewidth=0.25)

		for point in self.points:
			plt.scatter(point.x, point.y, color='red', s=2.0)
		# if Name is not None:
		# 	plt.savefig(Name,dpi=600)
		fig.show()
