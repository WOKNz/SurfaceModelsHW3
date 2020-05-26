import numpy as np
import matplotlib.pyplot as plt

class Point():
	"""
	Point Obejct 3 dimensions and id
	"""

	def __init__(self, x, y, z, id=None):
		"""

		:param x: value x of the point
		:type x: float
		:param y:value y of the point
		:type y: float
		:param z:value z of the point
		:type z: float
		:param id: The id of a point
		:type id: str
		"""
		self.x = x
		self.y = y
		self.z = z
		self.id = id

	def __str__(self):
		if self.id is None:
			return '(' + str(self.x) + ',' + str(self.y) + ')'
		else:
			return str(self.id)
		# return str(self.id) + ' (' + str(self.x) + ',' + str(self.y) + ')'

	@staticmethod
	def npArrayToListOfPoints(points):
		"""
		Convert ndarray to list of Points
		:param points: array of points (x,y,z)
		:type points:  ndarray
		:return: list of Point objects
		:rtype: list
		"""
		id_index = 0
		temp_list = []
		if points is None:
			return
		if points.shape[1] == 2:
			for row in range(points.shape[0]):
				temp_list.append(Point(points[row, 0], points[row, 1], None, str(id_index)))
				id_index = id_index + 1
		if points.shape[1] == 3:
			for row in range(points.shape[0]):
				temp_list.append(Point(points[row, 0], points[row, 1], points[row, 2], str(id_index)))
				id_index = id_index + 1
		return temp_list


class Triangle():
	"""
	Triangle class hold triangle data
	"""

	def __init__(self, p1, p2, p3, tri_p1=None, tri_p2=None, tri_p3=None, id=None):
		"""

		:param p1: Corner 1 of a triangle
		:type p1: Point
		:param p2: Corner 2 of a triangle
		:type p2: Point
		:param p3: Corner 3 of a triangle
		:type p3: Point
		:param tri_p1: Triangle that in front of p1
		:type tri_p1: Triangle
		:param tri_p2: Triangle that in front of p1
		:type tri_p2: Triangle
		:param tri_p3: Triangle that in front of p1
		:type tri_p3: Triangle
		:param id: Id of a triangle
		:type id: str
		"""
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
			return str(self.id) + \
			       ' (' + \
			       str(self.p1.id) + \
			       ',' + \
			       str(self.p2.id) + \
			       ',' + \
			       str(self.p3.id) + ']'

	def match(self, point):
		"""
		Function that matches the corners of two triangles at specific way (Look in HW3.pdf)

		:param point: Point that have the second triangle as in front triangle
		:type point: Point
		:rtype: None
		"""

		def oposite(self):
			"""
			Function that searches in second triangle the point that opposite to give point in first triangle

			:param self: origin triangle
			:type self: Triangle
			:return: point that in front
			:rtype: Point
			"""
			if self.tri_p1 is None:
				return None
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
		if op is not None:
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
		"""
		Flips two triangles

		:param point: point in front of infront triangle (point in origin triangle)
		:type point:  Point
		:rtype: None
		"""

		def updateInFrontOfInfrontTriangle(self, point_str, triangle_to_set):
			"""
			Updates the references in infront triangle

			:param self: origin triangle
			:type self: Triangle
			:param point_str: origin point
			:type point_str: Point
			:param triangle_to_set: in front triangle
			:type triangle_to_set: Triangle
			:rtype: None
			"""
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

		# Look in HW3.pdf for the algorithm
		thisTri.tri_p1 = b
		thisTri.tri_p2 = otherTri
		otherTri.tri_p1 = c
		otherTri.tri_p3 = thisTri

		thisTri.p3 = otherTri.p1
		otherTri.p2 = thisTri.p1

	def isInCircle(self, point):
		"""
		Checks if the point is inside covering circle io the triangle

		:param point: in front point
		:type point: Point
		:return: True = inside or on the line of the circle , False = outside
		:rtype: bool
		"""

		def oposite(self):  # Repeated code, make sure you use after match()
			if self.tri_p1 is None:
				return None
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
			"""
			Checks if the points of the triangle is in ccw order

			:param self: a triangle been checked
			:type self: Triangle
			:return: True = ccw or on the same line
			:rtype: bool
			"""
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
		"""
		Function that calls for match() and checks if flip is needed

		:param point: in front point
		:type point: Point
		:return: True = need to be fliped
		:rtype: bool
		"""
		self.match(point)
		if self.tri_p1 is None:
			return 0
		if self.isInCircle(point):
			self.flip(point)
			return 1
		else:
			return 0

	def updateInFrontOfInfrontTriangle(self, point_str, triangle_to_set):  # Repeated Code
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


class DelaunoyTriangulation():
	"""
	Delanoy triangulation databse and relevant functions
	"""

	def __init__(self, points):
		"""

		:param points: list of points that need to be triangulated

		:type points: list
		"""
		self.j = 0
		self.points = Point.npArrayToListOfPoints(points)
		self.triangles = None

		# Bounding box dimensionsz
		width = np.max(points[:, 0]) - np.min(points[:, 0])
		higth = np.max(points[:, 1]) - np.min(points[:, 1])
		M = max((width, higth))

		# Center of Mass (points)
		x_c = np.average(points[:, 0])
		y_c = np.average(points[:, 1])

		# Corners of covering triangle
		self.big_tri_p1 = Point(x_c + 20 * M, y_c, 0, id='B1')
		self.big_tri_p2 = Point(x_c, y_c + 20 * M, 0, id='B2')
		self.big_tri_p3 = Point(x_c - 20 * M, y_c - 20 * M, 0, id='B3')
		self.triangles = [Triangle(self.big_tri_p1,
		                           self.big_tri_p2,
		                           self.big_tri_p3,
		                           id='T0')]

		# Splitting triangle that new point falls into f
		for point in self.points:
			self.split(point, self.inWhichTriangle(point))

		self.fixTriangulation()
		self.cleanOutter()

	# Export
	# self.saveTriangles('triangles_data.xyz')

	def split(self, pointA, triangle):
		"""
		Splitting Triangle into three triangles

		:param pointA: new point that splits
		:type pointA: Point
		:param triangle: relevant triangle that the point is inside
		:type triangle: Triangle
		:rtype: None
		"""

		# Empty case
		if triangle is None:
			return

		# Creating three new triangles
		temp_trianle1A2 = Triangle(triangle.p1, pointA, triangle.p2)
		temp_trianle2A3 = Triangle(triangle.p2, pointA, triangle.p3)
		temp_trianle3A1 = Triangle(triangle.p3, pointA, triangle.p1)

		# adding proper properties
		temp_trianle1A2.tri_p1 = temp_trianle2A3
		temp_trianle1A2.tri_p3 = temp_trianle3A1
		temp_trianle2A3.tri_p1 = temp_trianle3A1
		temp_trianle2A3.tri_p3 = temp_trianle1A2
		temp_trianle3A1.tri_p1 = temp_trianle1A2
		temp_trianle3A1.tri_p3 = temp_trianle2A3

		temp_trianle1A2.tri_p2 = triangle.tri_p3
		temp_trianle2A3.tri_p2 = triangle.tri_p1
		temp_trianle3A1.tri_p2 = triangle.tri_p2

		temp_trianle1A2.updateInFrontOfInfrontTriangle('p2', temp_trianle1A2)
		temp_trianle2A3.updateInFrontOfInfrontTriangle('p2', temp_trianle2A3)
		temp_trianle3A1.updateInFrontOfInfrontTriangle('p2', temp_trianle3A1)

		temp_trianle1A2.id = 'T' + str(self.j + 1)
		temp_trianle2A3.id = 'T' + str(self.j + 2)
		temp_trianle3A1.id = 'T' + str(self.j + 3)
		self.j = self.j + 3

		# adding new triangles to the list
		self.triangles.extend([temp_trianle1A2, temp_trianle2A3, temp_trianle3A1])
		# removing the splited triangle
		self.triangles.remove(triangle)

	def fixTriangulation(self):
		"""
		Cheking if there is triangles to flip until there 0 to flip over the list
		:rtype: None
		"""
		stop = 1
		while stop > 0:
			stop = 0
			# self.plotDiagramm(limits=[2.5,-3,2.5,-2.5])
			for triangle in self.triangles:
				# self.plotDiagramm(limits=[2.5,-3,2.5,-2.5])
				stop = stop + triangle.isFlip(triangle.p1)
				# self.plotDiagramm(limits=[2.5,-3,2.5,-2.5])
				stop = stop + triangle.isFlip(triangle.p2)
				# self.plotDiagramm(limits=[2.5,-3,2.5,-2.5])
				stop = stop + triangle.isFlip(triangle.p3)
			# self.plotDiagramm(limits=[2.5,-3,2.5,-2.5])
			# if stop > 0:
			# 	break

	@staticmethod
	def isInsideTriangle(point, triangle):
		"""
		Cheking if the point is inside the triangle

		:param point: checked point
		:type point: Point
		:param triangle: checked triangle
		:type triangle: Triangle
		:return: True = inside
		:rtype: bool
		"""

		def ccw(pA, pB, pC):  # Repeated code
			temp_mat = np.array([[pA.x, pA.y, 1],
			                     [pB.x, pB.y, 1],
			                     [pC.x, pC.y, 1]])
			det = np.linalg.det(temp_mat)
			if det > 0:
				return True
			elif det == 0:
				print('all points on same line')
				return True
			else:
				return False

		if (ccw(triangle.p1, triangle.p2, point) and \
		    ccw(triangle.p2, triangle.p3, point) and \
		    ccw(triangle.p3, triangle.p1, point)) or \
				(not ccw(triangle.p1, triangle.p2, point) and \
				 not ccw(triangle.p2, triangle.p3, point) and \
				 not ccw(triangle.p3, triangle.p1, point)):
			return True
		else:
			return False

	def inWhichTriangle(self, point):
		"""
		Going over the list of triangle and checking if the point is inside

		:param point: checked point
		:type point: Point
		:return: relevant triangle
		:rtype: Triangle
		"""
		for triangle in self.triangles:
			if DelaunoyTriangulation.isInsideTriangle(point, triangle):
				return triangle

	def cleanOutter(self):
		"""
		Goes over all triangles in the list and delete those who have covering triangle points
		:rtype: None
		"""
		max_len = len(self.triangles)
		triangles_to_keep = []

		for i in range(0, max_len):
			if self.big_tri_p1 is self.triangles[i].p1 or \
					self.big_tri_p1 is self.triangles[i].p2 or \
					self.big_tri_p1 is self.triangles[i].p3 or \
					self.big_tri_p2 is self.triangles[i].p1 or \
					self.big_tri_p2 is self.triangles[i].p2 or \
					self.big_tri_p2 is self.triangles[i].p3 or \
					self.big_tri_p3 is self.triangles[i].p1 or \
					self.big_tri_p3 is self.triangles[i].p2 or \
					self.big_tri_p3 is self.triangles[i].p3:
				continue
			else:
				if len(self.triangles) > 0:
					triangles_to_keep.append(self.triangles[i])
		self.triangles = triangles_to_keep

	def plotDiagramm(self, Name=None, unpad=None, limits=None):
		"""
		Plotting diagram of the triangles and points

		:param Name: Name of the file if you want to save the plot
		:type Name: str
		:param unpad: Padding to the triangles (seperates them) 0.2 is good
		:type unpad: float
		:param limits: Limits of the plot
		:type limits: list
		:rtype: None
		"""
		fig = plt.figure()

		def addRadilBias(triangle, unpad):
			tt = Triangle(triangle.p1, triangle.p2, triangle.p3)  # temp triangle
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
				plt.text(center[0], center[1], triangle.id, fontsize=5)
		else:
			for triangle in self.triangles:
				plt.plot([triangle.p1.x, triangle.p2.x, triangle.p3.x, triangle.p1.x],
				         [triangle.p1.y, triangle.p2.y, triangle.p3.y, triangle.p1.y], linewidth=0.25)

		for point in self.points:
			plt.scatter(point.x, point.y, color='red', s=0.2)
		# plt.text(point.x, point.y, point.id, fontsize=9)
		if Name is not None:
			plt.savefig(Name, dpi=600)
		if limits is not None:
			plt.xlim(right=limits[0])  # xmax is your value
			plt.xlim(left=limits[1])  # xmin is your value
			plt.ylim(top=limits[2])  # ymax is your value
			plt.ylim(bottom=limits[3])  # ymin is your value
		fig.show()

	def saveTriangles(self, name):
		"""
		Exporting the triangles to .txt file (p1 ,p2 ,p3)

		:param name: Name of the file to be saved
		:type name: str
		:return: saves file
		"""
		temp_np = np.zeros((len(self.triangles), 3), dtype=int)
		for i in range(len(self.triangles)):
			temp_np[i, :] = np.array([self.triangles[i].p1.id, self.triangles[i].p2.id, self.triangles[i].p3.id])
		np.savetxt(name, temp_np, fmt='%i')
