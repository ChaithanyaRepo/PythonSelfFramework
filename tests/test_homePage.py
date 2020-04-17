import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        logs = self.getLogger()

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["Name"])
        logs.info("Name : "+getData["Name"])
        homePage.getEmail().send_keys(getData["Email"])
        logs.info("Email : "+getData["Email"])
        homePage.getPassword().send_keys(getData["Password"])
        logs.info("Password : "+getData["Password"])
        homePage.getIceCream().click()
        self.selectOptionByText(homePage.getGender(), getData["Gender"])
        logs.info("Gender : "+getData["Gender"])
        homePage.getEmployeeStatus().click()
        logs.info("IceCream : Checked")
        # homePage.getDateOfBirth().send_keys(getData["DOB"])
        # logs.info("Date Of Birth : "+getData["DOB"])
        homePage.getFormSubmit().click()
        logs.info("Submit")

        alertMsg = homePage.getSuccessMsg().text
        assert ("Success" in alertMsg)
        logs.info(alertMsg)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData(""))
    def getData(self, request):
        self.getLogger().info("Data request")
        return request.param
