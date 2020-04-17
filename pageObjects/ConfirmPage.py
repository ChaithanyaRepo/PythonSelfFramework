from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    enterDeliveryCountry = (By.CSS_SELECTOR, "input[class*='validate']")
    deliveryPlaces = (By.LINK_TEXT, "India")
    selectDeliveryCountry = (By.LINK_TEXT, "India")
    checkBox = (By.CSS_SELECTOR, "div[class*='checkbox']")
    submit = (By.XPATH, "//input[contains(@class,'btn')]")
    alertMsg = (By.XPATH, "//div[contains(@class,'alert')]")

    def getEnterDeliveryCountry(self):
        # self.driver.find_element_by_css_selector("input[class*='validate']")
        return self.driver.find_element(*ConfirmPage.enterDeliveryCountry)

    def getDeliveryPlaces(self):
        # self.driver.find_elements_by_link_text("India")
        return self.driver.find_elements(*ConfirmPage.deliveryPlaces)

    def getSelectDeliveryPlace(self):
        # self.driver.find_element_by_link_text("India").click()
        return self.driver.find_element(*ConfirmPage.selectDeliveryCountry)

    def getCheckBox(self):
        # self.driver.find_element_by_css_selector("div[class*='checkbox']").click()
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmit(self):
        # self.driver.find_element_by_xpath("//input[contains(@class,'btn')]").click()
        return self.driver.find_element(*ConfirmPage.submit)

    def getAlertMsg(self):
        # alertMsg = self.driver.find_element_by_xpath("//div[contains(@class,'alert')]").text
        return self.driver.find_element(*ConfirmPage.alertMsg)
