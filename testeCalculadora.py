import unittest

class TesteCalculadora(unittest.TestCase):
	def test_somar(self):
		from calculadora import somar
		self.assertEqual(somar(1,1), 2)

	def test_multiplicar(self):
		from calculadora import multiplicar
		self.assertEqual(multiplicar(2,3), 6)

unittest.main()