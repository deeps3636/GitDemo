import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):

        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getPassword().send_keys("12345")
        time.sleep(1)
        homepage.getcheck().click()

        homepage.getSubmit().click()

        time.sleep(1)

        self.selectOptionByText(homepage.getGender(),getData[2])  # This methgod can be used for any dropdown
        homepage.getBinder().send_keys("Hi")
        time.sleep(3)
        msg = homepage.getAlertMsg().text
        print(msg)

        assert "Success" in msg
        time.sleep(2)
        self.driver.refresh()
    @pytest.fixture(params=[("Deepak","deeps@gmail.com","Male"),("Shonima","sh@gmal.com","Female")])
    def getData(self,request):
        return request.param
