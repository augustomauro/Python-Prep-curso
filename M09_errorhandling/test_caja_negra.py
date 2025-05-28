import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

    def test_esta_suma_deberia_fallar(self):
        num_1 = 2
        num_2 = 3

        resultado = suma(num_1, num_2) - 1

        self.assertEqual(resultado, 5)  # AssertionError: 4 != 5

unittest.main(argv=[''], verbosity=2, exit=False)