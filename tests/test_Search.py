import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Search(unittest.TestCase):
    def setUp(self):
        selenium_grid_url = "http://localhost:4444/wd/hub"
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = "LINUX"
        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                command_executor=selenium_grid_url)
        self.driver.get("http://www.google.com")

        self.assertTrue("Google" in self.driver.title)

    def test_char_search(self):
        test = "p"

        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys(test)
        input_element.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_word_search(self):
        test = "python"

        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys(test)
        input_element.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_256chars_search(self):
        test = 'pythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpython' \
               'pythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpython' \
               'pythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpython' \
               'pyth'

        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys(test)
        input_element.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_negative_number_search(self):
        test = "-1000000"

        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys(test)
        input_element.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_positive_number_search(self):
        test = "1000000"

        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys(test)
        input_element.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
