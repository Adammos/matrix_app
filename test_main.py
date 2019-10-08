import pytest

from main import Matrix 

#@pytest.mark.xfail
class TestInputWidthAndHeight:
	def setup_method(self, method):
		self.matrix = Matrix()

	def test_valid_values(self):
		self.matrix.width = '5'
		self.matrix.height = '6'

	def test_empty_value(self):
		with pytest.raises(ValueError):
			self.matrix.width = ''

		with pytest.raises(ValueError):	
			self.matrix.height = ''

	def test_zero(self):
		with pytest.raises(ValueError):
			self.matrix.width = '0'

		with pytest.raises(ValueError):
			self.matrix.height = '0'

	def test_float_value(self):
		with pytest.raises(ValueError):
			self.matrix.width = '2.2'

		with pytest.raises(ValueError):
			self.matrix.height = '2.2'

	def test_NaN_value_type(self):
		with pytest.raises(ValueError):
			self.matrix.width = 'a'

		with pytest.raises(ValueError):
			self.matrix.height = 'a'

	def test_negative_value(self):
		with pytest.raises(ValueError):
			self.matrix.width = '-10'

		with pytest.raises(ValueError):
			self.matrix.height = '-10'

	def test_multiple_values(self):
		with pytest.raises(ValueError):
			self.matrix.width = '1 2'

		with pytest.raises(ValueError):
			self.matrix.height = '1 2'


class TestAppendDataToMatrix:
	def setup_method(self, method):
		self.matrix = Matrix()
		self.matrix.width = 2
		self.matrix.height = 3
	
	def test_valid_data(self):
		self.matrix.append('1 3')
		self.matrix.append('23 -1')
		self.matrix.append('0 -345')

	def test_width_invalid_len_of_data_entered(self):
		with pytest.raises(ValueError):	
			self.matrix.append('')

		with pytest.raises(ValueError):	
			self.matrix.append('1')

		with pytest.raises(ValueError):	
			self.matrix.append('1 2 3')

	def test_height_invalid_len_of_data_entered(self):
		with pytest.raises(ValueError):
			self.matrix.append('1 3')
			self.matrix.append('1 3')
			self.matrix.append('1 3')
			self.matrix.append('1 3')

	def test_invalid_data_type(self):
		with pytest.raises(ValueError):	
			self.matrix.append('a b')

		with pytest.raises(ValueError):	
			self.matrix.append('1 x')

class TestMultiply:
	def setup_method(self, method):
		self.matrix_a = Matrix()
		self.matrix_a.width = 2
		self.matrix_a.height = 3
		self.matrix_a.append('1 2')
		self.matrix_a.append('5 3')
		self.matrix_a.append('6 7')

	
	def test_valid_matrix_dimensions(self):
		matrix_b = Matrix()
		matrix_b.width = 1
		matrix_b.height = 2
		matrix_b.append('5')
		matrix_b.append('1')

		self.matrix_a.multiply(matrix_b)
		
	def test_valid_result(self):
		matrix_b = Matrix()
		matrix_b.width = 1
		matrix_b.height = 2
		matrix_b.append('5')
		matrix_b.append('1')
		
		matrix_c = self.matrix_a.multiply(matrix_b)	
		assert matrix_c.data == [[7,], [28,], [37,]]

	def test_invalid_matrix_b_height(self):
		matrix_b = Matrix()
		matrix_b.width = 1
		matrix_b.height = 3
		matrix_b.append('1')
		matrix_b.append('2')
		matrix_b.append('3')

		with pytest.raises(ValueError):
			self.matrix_a.multiply(matrix_b)
		
