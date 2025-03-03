import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self):

        homepage = HomePage(self.driver)

        homepage.getName().send_keys("Deepak")
        homepage.getEmail().send_keys("dds@gmail.com")
        homepage.getPassword().send_keys("12345")
        time.sleep(1)
        homepage.getcheck().click()
        # driver.find_element(By.ID, "exampleCheck1").click()
        #driver.find_element(By.NAME, "email").send_keys("dds@gmail.com")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        #homepage.getcheck().click()
        #driver.find_element(By.ID, "exampleCheck1").click()
        homepage.getSubmit().click()
        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # msg = driver.find_element(By.XPATH,"//").text
        #homepage.geempStatus.click()
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        # dropdown
        time.sleep(1)

        self.selectOptionByText(homepage.getGender(),"Male")  # This methgod can be used for any dropdown
        #dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Male")
        # dropdown.select_by_index()
        # dropdown.select_by_value() if the html tag has value, then that value cane be inserted here

        homepage.getBinder().send_keys("Hi")
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3])".send_keys("Hi")
        time.sleep(3)

        msg = homepage.getAlertMsg().text
        #msg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        print(msg)

        assert "Success" in msg
        time.sleep(5)


print("Added lins for git tests")


