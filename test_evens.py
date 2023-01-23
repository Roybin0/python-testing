import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def throw_error_if_no_value(self):
        self.assertRaises(TypeError, even_number_of_evens)

    def test_for_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


unittest.main()
