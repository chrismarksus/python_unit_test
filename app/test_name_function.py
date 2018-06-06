import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py"""

    def test_first_last_name(self):
        """ Do name like Janis Joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# You need this if line if you are going to use python3 -m unittest discover
# If not you get a fatal: empty ident name not allowed error but you will
# not get the error if you call the file with python3 test_file_name.py -v
if __name__ == '__main__':
    unittest.main()
