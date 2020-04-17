import inspect
import logging
import sys

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        if text == "India":
            wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, text)))
        elif text == "Success! Thank you!":
            wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='alert']")))

    def selectOptionByText(self, locator, text):
        if text == "":
            raise AttributeError
        elif text == "Male" or text == "Female":
            gender = Select(locator)
            gender.select_by_visible_text(text)
        elif text is not "Male" or text is not "Female":
            raise ValueError

    def getLogger(self):
        # To get actual file name of the test file
        loggerName = inspect.stack()[1][3]
        # log file object = enabling the file logging
        logger = logging.getLogger(loggerName)

        # Log file object = log file name/file where logs to be stored
        fileHandler = logging.FileHandler('../logsReports/Logfile.log', mode='w')
        # log file object  = Setting log file format
        logFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(logFormatter)

        # File handler object
        logger.addHandler(fileHandler)

        # Setting the log level
        logger.setLevel(logging.DEBUG)

        return logger
