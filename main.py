import sys

class Matrix:
	def __init__(self):
		
		self._width = None
		self._height = None
		
		self.data = [] 

	@property 
	def width(self):
		return self._width 

	@property 
	def height(self):
		return self._height

	@width.setter
	def width(self, value):
		try:
			self._width = int(value)
			if self.width <= 0:
				raise ValueError 
		except ValueError:
			raise ValueError(f'Invalid width value: <{value}>.')
	
	@height.setter
	def height(self, value):
		try:
			self._height = int(value)
			if self.height <= 0:
				raise ValueError
		except ValueError:
				raise ValueError(f'Invalid height value: <{value}>.')

	def set_size(self):
		'''
		Sets the matrix size from data collected from the user.
		'''
		width = input('width: ')
		self.width = width

		height = input('height: ')
		self.height =height
		print()


	def set_data(self):
		'''
		Fills the matrix with data collected from the user.
		'''
		for i in range(self.height):
			data = input()
			self.append(data)
		print()


	def append(self, data):
		'''
		Appends to the matrix new row of data collected from the user.
		'''
		# Check data against the matrix height
		if len(self.data) >= self.height:
			raise ValueError(f'You cannot enter more data, the height <{self.height}> was exceeded!')

		# Check data against the matrix width
		data = data.split()
		if len(data) != self.width:
			raise ValueError(f'Number of arguments: <{len(data)}> does not fit the width of the matrix.')		
		try:
			# Check the data type of the entered data
			data = [int(number) for number in data]	
			self.data.append(data)
		except ValueError:
			raise ValueError(f'Invalid type in the argument: <{data}>.')


	def multiply(self, matrix_other):
		''' 
		Returns a new matrix that is a result of the self matrix multiplied by the matrix passed in 
		the argument.
		'''

		# Create empty C matrix
		matrix_c = Matrix()
		matrix_c.width = matrix_other.width
		matrix_c.height = self.height
		for row in range(matrix_c.height):
			matrix_c.data.append([0 for cell in range(matrix_c.width)])

		# Check for correct dimensions
		if self.width != matrix_other.height:
			raise ValueError(f'Wrong dimensions, Matrix A cannot be multiplied by Matrix B.')

		# Execute the multiplication
		for row in range(matrix_c.height):
			for col in range(matrix_c.width):
				val = 0
				for i in range(self.width):
					val += self.data[row][i] * matrix_other.data[i][col]
				matrix_c.data[row][col] = val 
		return matrix_c


	def __repr__(self):
		list_row_strings = []
		for row in self.data:
			row_string = ' '.join(str(cell) for cell in row)
			list_row_strings.append(row_string)
		return '\n'.join(list_row_strings) 


if __name__ == '__main__':
	print('Welcome to Matrix multiplication script.')

	'''	
	matrix_test = Matrix()
	matrix_test.data = [[1, 2], [3, 4], [5, 6], [7, 8]]
	print(matrix_test)
	sys.exit()
	'''
	try:
		print('Matrix A')
		matrix_a = Matrix()
		matrix_a.set_size()

		print('Matrix B')
		matrix_b = Matrix()
		matrix_b.set_size()

		print('Matrix  A values: ')
		matrix_a.set_data()	

		print('Matrix B values: ')
		matrix_b.set_data()

		result = matrix_a.multiply(matrix_b)
		print('Result: ')
		print(result)
	except ValueError as e:
		print(e)