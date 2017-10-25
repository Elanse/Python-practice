import unittest
try:
    import tools
except ImportError:
    pass



class BoolExercises(unittest.TestCase):

    def test_module_exists(self):
        try:
            import tools
            exists = True
        except ImportError:
            exists = False

        error_msg = '\nMake sure you have put your functions in ' +\
            'a file named tools.py'
        self.assertTrue(exists, msg=error_msg)

    def test_three_or_four(self):
        error_msg = '\nWrite a function named `three_or_four` that takes\n' +\
            'a single number and returns True if the number is divisible\n' +\
            'by three or four, and False otherwise.'
        self.assertTrue(tools.three_or_four(4), msg=error_msg)
        self.assertTrue(tools.three_or_four(3), msg=error_msg)
        self.assertTrue(tools.three_or_four(12), msg=error_msg)
        self.assertTrue(tools.three_or_four(15), msg=error_msg)
        self.assertTrue(tools.three_or_four(20), msg=error_msg)
        self.assertFalse(tools.three_or_four(5), msg=error_msg)
        self.assertFalse(tools.three_or_four(22), msg=error_msg)

    def test_long_word(self):
        error_msg = '\nWrite a function named `long_word` that returns\n' +\
            'True if the single parameter `word` is a string longer than 8,\n'+\
            'False if it is shorter, and None if `word` is an empty string.'

        self.assertTrue(tools.long_word('abcdefghi'), msg=error_msg) #9 chars
        self.assertFalse(tools.long_word('abcdefgh'), msg=error_msg) # 8 chars
        self.assertFalse(tools.long_word('abc'), msg=error_msg)
        self.assertIsNone(tools.long_word(''), msg=error_msg)

    def test_leap_year(self):
        error_msg = 'A year is a leap year if it is divisible by 4 unless\n' +\
            'it is a century that is not divisible by 400.  Write a\n' +\
            'function that takes a year as a parameter and returns True\n'+\
            'if the year is a leap year, and False otherwise.\n'

        self.assertFalse(tools.leap_year(2001), msg=error_msg) #not divisible by 4
        self.assertTrue(tools.leap_year(2004), msg=error_msg)  #divisible by 4
        self.assertFalse(tools.leap_year(2100), msg=error_msg) #century not divisible by 400
        self.assertTrue(tools.leap_year(2800), msg=error_msg)  #century divisible by 400

    def test_larger_number(self):
        error_msg = 'Write a function that returns the larger of two\n' +\
            'numbers or None if the numbers are equal.'

        self.assertEqual(tools.larger_number(1,2), 2, msg=error_msg)
        self.assertEqual(tools.larger_number(2, 1), 2, msg=error_msg)
        self.assertIsNone(tools.larger_number(1, 1), msg=error_msg)
        self.assertEqual(tools.larger_number(-5, -2), -2, msg=error_msg)
        self.assertIsNone(tools.larger_number(0, 0), msg=error_msg)

    def test_get_letter_grade(self):
        error_msg = 'Write a function that returns the letter grade for a\n' +\
            'given percentage. Use your school\'s grading scale and return\n' +\
            'capital letters (no plus/minus).'

        self.assertEqual(tools.get_letter_grade(100), 'A', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(90), 'A', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(89.9), 'B', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(80), 'B', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(75), 'C', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(70), 'C', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(65), 'D', msg=error_msg)
        self.assertEqual(tools.get_letter_grade(55), 'F', msg=error_msg)

    def test_sum_first(self):
        error_msg = 'Write a function that returns the sum of the first\n' +\
            'n numbers where n is a parameter. Use the accumulator pattern.'

        self.assertEqual(tools.sum_first(5), 15, msg=error_msg)
        self.assertEqual(tools.sum_first(0), 0, msg=error_msg)

    def test_accumulate(self):
        error_msg = 'Write a function that returns the sum of a list of\n' +\
            'numbers and 0 for an empty list. Loop through the list\n'+\
            'and use the accumulator pattern\n'

        self.assertEqual(tools.accumulate([3]), 3)
        self.assertEqual(tools.accumulate([3, 5, 9]), 17)
        self.assertEqual(tools.accumulate([]), 0)

unittest.main(verbosity=2)
