import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckOutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Testone(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        #setup.driver.implicitly_wait(5)
        homePage.shopItems().click()
        #confirmPage =homePage.shopItems()  This can be used to invoke checkout from checkout page instead of invoking from confirm
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting the all the card title")
        products = checkOutPage.getCardTitles()
        self.driver.implicitly_wait(5)

        #cardFooter = checkOutPage.getCardTitles()
        cardProduct = checkOutPage.getProduct()
        selectProduct = checkOutPage.getCardSelect()
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        time.sleep(2)
        #products = self.driver.find_elements(By.XPATH, "//app-card/div")
        # products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

        for product in products:

            #if checkOutPage.getCardFooter().text == "Blackberry":
            if product.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                #prodText = product.text
                log.info(product.find_element(By.XPATH, "div/h4/a").text)

                product.find_element(By.XPATH, "div/button").click()

                #checkOutPage.selectProduct.click()
                #self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
                break

        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        # driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering country name 'Ind'")
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)
        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success" in success


