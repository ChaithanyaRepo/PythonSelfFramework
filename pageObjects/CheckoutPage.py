from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.CSS_SELECTOR, "h4.card-title a")
    cardFooter = (By.CSS_SELECTOR, "div.card-footer button")
    productTitle = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    checkOut = (By.CSS_SELECTOR, "a[class*=btn]")
    productName = (By.LINK_TEXT, "Blackberry")
    addItem = (By.CSS_SELECTOR, "input[type='number']")
    confirmItem = (By.CSS_SELECTOR, "button[class*=btn-success]")

    def getCardTitles(self):
        # products = self.driver.find_element_by_css_selector("h4.card-title a")
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        # product.find_element_by_css_selector("div.card-footer button")
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getProductTitle(self):
        # productNamePg1 = product.find_element_by_xpath("//div/h4/a").text
        return self.driver.find_element(*CheckOutPage.productTitle)

    def getCheckOut(self):
        # driver.find_element_by_css_selector("a[class*=btn]").click()
        return self.driver.find_element(*CheckOutPage.checkOut)

    def getProductName(self):
        # productNamePg2 = self.driver.find_element_by_link_text("Blackberry")
        return self.driver.find_element(*CheckOutPage.productName)

    def getAddItem(self):
        # self.driver.find_element_by_css_selector("input[type='number']").clear()
        # self.driver.find_element_by_css_selector("input[type='number']").send_keys("2")
        return self.driver.find_element(*CheckOutPage.addItem)

    def getConfirmItem(self):
        # self.driver.find_element_by_css_selector("button[class*=btn-success]").click()
        self.driver.find_element(*CheckOutPage.confirmItem).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
