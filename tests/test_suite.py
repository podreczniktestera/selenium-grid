import unittest
from test_Search import Search


def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(Search('test_char_search'))
    suite.addTest(Search('test_word_search'))
    suite.addTest(Search('test_256chars_search'))
    suite.addTest(Search('test_negative_number_search'))
    suite.addTest(Search('test_positive_number_search'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())