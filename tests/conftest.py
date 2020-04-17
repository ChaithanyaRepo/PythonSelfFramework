from logging import getLogger

import pytest
from selenium import webdriver

driver = None

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--ignore-certificate-errors")

firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.add_argument("--start-maximized")
firefoxOptions.add_argument("--ignore-certificate-errors")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="please specify the browser"
        # To provide URL in the runtime add another field same as browser and specify URL during build trigger
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome" or browser_name == "CHROME":
        driver = webdriver.Chrome(
            executable_path='/home/chaitanya/Documents/software/drivers/chromedriver_linux64/chromedriver',
            options=chromeOptions)
    elif browser_name == "firefox" or browser_name == "FIREFOX":
        driver = webdriver.Firefox(
            executable_path='/home/chaitanya/Documents/software/drivers/geckodriver-v0.26.0-linux64/geckodriver',
            options=firefoxOptions)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    # If a plugin wants to collaborate with code from another plugin it can obtain a reference through the plugin manager
    # Collaborating one plugin with code with help of another plugin through plugin manager
    pytest_html = item.config.pluginmanager.getplugin('html')
    # Performing all the actions required before next hook executes
    outcome = yield
    # Return the result
    report = outcome.get_result()
    # getattr(object, attribute, default)
    # object - Required. An object.
    # attribute - The name of the attribute you want to get the value from
    # default - Optional. The value to return if the attribute does not exist
    extra = getattr(report, 'extra', [])

    # Executing the fun when report called or setup
    if report.when == 'call' or report.when == "setup":
        # Syntax : hasattr(obj, key)
        # Parameters :
        # obj : The object whose which attribute has to be checked.
        # key : Attribute which needs to be checked.
        # Returns : Returns True, if attribute is present else returns False.
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Creating the screenshot name based on concatenation of (Package name + Class name + Method name)
            file_name = report.nodeid.replace("::", "_") + ".png"
            # Calling fun to capture screenshot and storing it in the specified path
            capture_screenshot('../logsReports/Images/' + file_name)
            if file_name:
                # Defining the assets fo the image
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                # Attaching the captured screenshot to the test report
                extra.append(pytest_html.extras.html(html))
            # Appending the data from extra keyword to the report
            report.extra = extra


def capture_screenshot(name):
    # Capturing the screenshot
    # driver.save_screenshot(name)
    # driver.get_screenshot_as_png(name)  # try with init fun to resolve the issue
    driver.get_screenshot_as_file(name)
