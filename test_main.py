import unittest
from main import sumar

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(4, 6), 10)
        self.assertEqual(sumar(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
