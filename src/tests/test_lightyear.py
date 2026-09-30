import unittest
from oxrse_unit_conv.units import lightyear, m

class TestLightyear(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(lightyear.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(lightyear.to_si(1), 9.4607305e15)
        self.assertEqual(lightyear.to_unit(10, lightyear), 10)

if __name__ == '__main__':
    unittest.main()