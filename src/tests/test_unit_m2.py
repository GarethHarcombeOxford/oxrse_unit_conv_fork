import unittest
from oxrse_unit_conv.units import m2, m


class TestSquareMeter(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(m2.si_unit.matches(m))

    def test_to_si(self):
        self.assertEqual(m2.to_si(1), 1)
        self.assertEqual(m2.to_si(2), 4)

    def test_from_si(self):
        self.assertEqual(m.to_unit(9, m2), 3)


if __name__ == '__main__':
    unittest.main()
