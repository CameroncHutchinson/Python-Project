import unittest
import Project as Pjt


class TestProject(unittest.TestCase):
    """ Unit Test class that inherits unittest functions """
    code = Pjt.DataSet()

    def test_lines_loaded(self):
        """ Method that test whether Load File function loads correct number
         of lines
         """
        self.assertEqual(6147, TestProject.code.load_file(), "Unit Test"
                                                             " Failed")


if __name__ == '__main__':
    unittest.main()


r"""
--- Unit Test Sample Run ---
Number of lines loaded: 6147


Ran 1 test in 0.025s

OK

Process finished with exit code 0
"""





