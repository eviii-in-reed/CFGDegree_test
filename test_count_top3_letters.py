import unittest
from homeworks import three_common_letter


class MyTestCase(unittest.TestCase):
    def test_normal_case(self):
        tuple = ['a', 'o', 'y']
        assumed = three_common_letter("you are so beautiful today Merida")
        self.assertEqual(tuple, assumed)  # add assertion here

    def test_invalid_case(self):
        response = "There are no enough letter in the string to count for"
        assumed = three_common_letter("sq")
        self.assertEqual(response,assumed)
        




if __name__ == '__main__':
    unittest.main()
