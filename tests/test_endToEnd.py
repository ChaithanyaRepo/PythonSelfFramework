from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

productNamePg1 = None


class TestOne(BaseClass):

    def test_e2e(self):
        global productNamePg1
        logs = self.getLogger()

        # self.driver.find_element_by_link_text("Shop").click()
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()
        checkOutPage = homePage.shopItems()
        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        # products = self.driver.find_elements_by_css_selector("h4.card-title a")
        # checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()
        logs.info("Capturing all the product names")
        i = -1

        # //div[@class='card h-100']/div/h4/a
        # product = //div[@class='card h-100']
        for product in products:
            i = i + 1
            # productNamePg1 = product.text
            productNamePg1 = product.text

            if productNamePg1 == "Blackberry":
                # Add item to card
                # product.find_element_by_xpath("div/button").click()
                # product.find_element_by_css_selector("div.card-footer button")
                logs.info("Selecting only blackberry")
                checkOutPage.getCardFooter()[i].click()

        # Proceeding after item added to cart
        # self.driver.find_element_by_css_selector("a[class*=btn]").click()
        checkOutPage.getCheckOut().click()
        logs.info("Blackberry product checkout")

        # Collecting the title of product added to cart
        # productNamePg2 = self.driver.find_element_by_link_text("Blackberry").text
        productNamePg2 = checkOutPage.getProductName().text

        # Ensuring same product added to cart
        assert productNamePg1 == productNamePg2
        logs.info("Comparing the product selected")

        # Adding another item to cart
        # self.driver.find_element_by_css_selector("input[type='number']").clear()
        # self.driver.find_element_by_css_selector("input[type='number']").send_keys("2")
        checkOutPage.getAddItem().clear()
        checkOutPage.getAddItem().send_keys("2")
        logs.info("Adding another item to cart")

        # Confirming the added product to cart
        # self.driver.find_element_by_css_selector("button[class*=btn-success]").click()
        confirmPage = checkOutPage.getConfirmItem()

        # Selecting delivery location
        # self.driver.find_element_by_css_selector("input[class*='validate']").send_keys("India")
        # confirmPage = ConfirmPage(self.driver)
        confirmPage.getEnterDeliveryCountry().send_keys("India")
        logs.info("Selecting delivery country as India")

        # Waiting to location name to load
        self.verifyLinkPresence("India")

        # countries = self.driver.find_elements_by_link_text("India")
        countries = confirmPage.getDeliveryPlaces()
        for country in countries:
            print("Country", country.text)
            if country.text == "India":
                logs.info(country.text)
                country.click()
                break

        # self.driver.find_element_by_link_text("India").click()
        # confirmPage.getSelectDeliveryPlace().click()

        # Agree to T&C
        # self.driver.find_element_by_css_selector("div[class*='checkbox']").click()
        confirmPage.getCheckBox().click()

        # Checking the status of the checkbox
        # statusCheck = self.driver.find_element_by_css_selector("div[class*='checkbox']").is_enabled()
        statusCheck = confirmPage.getCheckBox().is_enabled()
        assert True == statusCheck
        logs.info("Agreeing the T&C conditions")

        # self.driver.find_element_by_xpath("//div[contains(@class,'checkbox')]").click()
        # statusCheck = self.driver.find_element_by_xpath("//div[contains(@class,'checkbox')]").is_enabled()
        # assert True == statusCheck

        # Proceed to next step
        # self.driver.find_element_by_css_selector("input[type='submit']").click()
        # self.driver.find_element_by_css_selector("input[class*='btn']").click()
        # self.driver.find_element_by_xpath("//input[contains(@class,'btn-lg')]").click()
        # self.driver.find_element_by_xpath("//input[contains(@class,'btn')]").click()
        confirmPage.getSubmit().click()
        logs.info("Ordering the product")

        # Wait until item visible
        # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='alert']")))
        self.verifyLinkPresence("Success! Thank you!")
        # alertMsg = self.driver.find_element_by_xpath("//div[contains(@class,'alert')]").text
        alertMsg = confirmPage.getAlertMsg().text

        # Check the alert message
        assert "Success! Thank you!" in alertMsg

        # Capturing the current screen
        # self.driver.get_screenshot_as_png()
        # self.driver.get_screenshot_as_file("screen.png")
        # self.driver.get_screenshot_as_base64()
        # self.driver.save_screenshot("screenCapture.png")
