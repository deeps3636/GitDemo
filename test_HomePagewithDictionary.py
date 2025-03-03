import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):

        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData["fname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys("12345")
        time.sleep(1)
        homepage.getcheck().click()

        homepage.getSubmit().click()

        time.sleep(1)

        self.selectOptionByText(homepage.getGender(),getData["gender"])  # This methgod can be used for any dropdown
        homepage.getBinder().send_keys("Hi")
        time.sleep(3)
        msg = homepage.getAlertMsg().text
        print(msg)

        assert "Success" in msg
        time.sleep(2)
        self.driver.refresh()
    # @pytest.fixture(params=[{"fname":"Deepak","email":"dds@gmail.com","gender":"Male"},{"fname":"Shonima","email":"shno@gmail.com","gender":"Female"}])
    # def getData(self, request):
    #     return request.param
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param