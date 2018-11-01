import unittest
from test_Search import Search

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(Search('test_cheese_search'))
    suite.addTest(Search('test_python_search'))
    suite.addTest(Search('test_selenium_search'))
    suite.addTest(Search('test_grid_search'))
    suite.addTest(Search('test_expo_search'))
    suite.addTest(Search('test_docker_search'))
    suite.addTest(Search('test_podrecznik_search'))
    suite.addTest(Search('test_testera_search'))
    suite.addTest(Search('test_000000_search'))
    suite.addTest(Search('test_2x2_search'))
    suite.addTest(Search('test_apple_search'))
    suite.addTest(Search('test_orange_search'))
    suite.addTest(Search('test_carrot_search'))
    suite.addTest(Search('test_tomato_search'))
    suite.addTest(Search('test_cucumber_search'))
    suite.addTest(Search('test_paint_search'))
    suite.addTest(Search('test_word_search'))
    suite.addTest(Search('test_excel_search'))
    suite.addTest(Search('test_power_search'))
    suite.addTest(Search('test_point_search'))
    suite.addTest(Search('test_fresh_search'))
    suite.addTest(Search('test_skype_search'))
    suite.addTest(Search('test_virtualbox_search'))
    suite.addTest(Search('test_vms_search'))
    suite.addTest(Search('test_chrome_search'))
    suite.addTest(Search('test_ie_search'))
    suite.addTest(Search('test_evernote_search'))
    suite.addTest(Search('test_mail_search'))
    suite.addTest(Search('test_firefox_search'))
    suite.addTest(Search('test_opera_search'))
    suite.addTest(Search('test_file_search'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())