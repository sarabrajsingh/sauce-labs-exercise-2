import unittest
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class RestApiTest(unittest.TestCase):

    def setUp(self):
        print("---TEST STARTING---")

        # service name is hardcoded - but could easily be parametrized with argparse
        command = ["minikube", "service", "sauce-labs-flask-api", "--url"]
        try:
            execution = subprocess.run(command, stdout=subprocess.PIPE)
        except Exception as e:
            raise(e)

        # declare and intialize instance variables
        self.serviceUrl = execution.stdout.decode('utf-8').rstrip()
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_driver = os.path.expanduser(
            '~') + "/.local/bin/chromedriver"
        self.driver = webdriver.Chrome(
            chrome_options=self.chrome_options, executable_path=self.chrome_driver)

        return super().setUp()

    # test case #1
    def test_greeting_at_root(self):
        print("---TEST1 - EXAMINING HTML BODY AT ROOT ENDPOINT (/)---")
        driver = self.driver

        # instantiate a wait object - useful for waiting for the k8s pods to spool up
        # wait = WebDriverWait(driver, 30)

        if not self.serviceUrl.endswith("/"):
            self.serviceUrl + "/"

        print("DEBUG={0}".format(self.serviceUrl))

        driver.get(self.serviceUrl)

        # wait until the text in our XPATH contains stuff
        # wait.until(ec.text_to_be_present_in_element((By.XPATH, '/html/body'), "Greetings Sauce Labs! Greetings from Raj!"))

        try:
            element = WebDriverWait(driver, 10).until(
                ec.text_to_be_present_in_element((By.XPATH, '/html/body'), 'Sauce Labs'))
        except AssertionError as ae:
            raise(ae)

        greeting = driver.find_element(By.XPATH, '/html/body')

        print("DEBUG={0}".format(greeting.text))

        # assert
        self.assertTrue(
            "Greetings Sauce Labs! Greetings from Raj!" in greeting.text)

    def tearDown(self):
        self.driver.close()
        print("---TEST FINISHED---")
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
