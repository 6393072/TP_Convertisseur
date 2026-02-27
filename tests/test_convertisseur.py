import unittest
from src.convertisseur import celsius_vers_fahrenheit, fahrenheit_vers_celsius, celsius_vers_kelvin, kelvin_vers_celsius

class TestConvertisseur(unittest.TestCase):
    def test_c_vers_f(self):        
        self.assertEqual(celsius_vers_fahrenheit(100),212)

    def test_c0_vers_f(self):
        self.assertEqual(celsius_vers_fahrenheit(0),32)

    def test_f_vers_c(self):
        self.assertEqual(fahrenheit_vers_celsius(68),20)

    def test_c_vers_k(self):
        self.assertEqual(celsius_vers_kelvin(36.6),309.75)

    def test_k_vers_c(self):
        self.assertEqual(kelvin_vers_celsius(273.15),0)

    def test_k_vers_c_exception(self):
        with self.assertRaises(ValueError): kelvin_vers_celsius(-320)

if __name__ == "__main__":
    unittest.main()