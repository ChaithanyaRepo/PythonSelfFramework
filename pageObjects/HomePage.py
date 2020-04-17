from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']:nth-child(2)")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@type='password']")
    icecream = (By.XPATH, "//input[@type='checkbox']")
    gender = (By.CSS_SELECTOR, "select[id*='example']")
    employee = (By.XPATH, "//div/input[@value='option2']")
    dob = (By.XPATH, "//div/input[@name='bday']")
    submit = (By.CSS_SELECTOR, "input[class*='btn-success']")
    alertMsg = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopItems(self):
        # self.driver.find_element_by_link_text("Shop")
        # return driver.find_element(*HomePage.shop)

        # driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getIceCream(self):
        return self.driver.find_element(*HomePage.icecream)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmployeeStatus(self):
        return self.driver.find_element(*HomePage.employee)

    # def getDateOfBirth(self):
    #     return self.driver.find_element(*HomePage.dob)

    def getFormSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.alertMsg)
