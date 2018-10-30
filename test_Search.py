import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Search(unittest.TestCase):

    def setUp(self):
        selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['platform'] = "LINUX"
        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                command_executor=selenium_grid_url)

        self.driver.get("http://www.google.com")

        self.assertTrue("Google" in self.driver.title)

    def test_cheese_search(self):
        test = "cheese!"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_python_search(self):
        test = "python"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_selenium_search(self):
        test = "selenium"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_grid_search(self):
        test = "grid"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_expo_search(self):
        test = "expo"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_docker_search(self):
        test = "docker"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_podrecznik_search(self):
        test = "podrecznik"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_testera_search(self):
        test = "testera"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_000000_search(self):
        test = "000000"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_2x2_search(self):
        test = "2x2"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_apple_search(self):
        test = "apple"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_orange_search(self):
        test = "orange"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_carrot_search(self):
        test = "carrot"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_tomato_search(self):
        test = "tomato"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_cucumber_search(self):
        test = "cucumber"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_paint_search(self):
        test = "paint"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_word_search(self):
        test = "word"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_excel_search(self):
        test = "excel"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_power_search(self):
        test = "power"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_point_search(self):
        test = "point"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_fresh_search(self):
        test = "fresh"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_skype_search(self):
        test = "skype"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_virtualbox_search(self):
        test = "virtualbox"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_vms_search(self):
        test = "vms"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_chrome_search(self):
        test = "chrome"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_ie_search(self):
        test = "ie"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_evernote_search(self):
        test = "evernote"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_mail_search(self):
        test = "mail"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_firefox_search(self):
        test = "firefox"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_opera_search(self):
        test = "opera"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def test_file_search(self):
        test = "file"

        inputElement = self.driver.find_element_by_name("q")
        inputElement.send_keys(test)
        inputElement.submit()

        WebDriverWait(self.driver, 10).until(EC.title_contains(test))
        self.assertTrue(test in self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
