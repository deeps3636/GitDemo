from selenium.webdriver.common.by import By


class CheckOutPage:
    cardTitle = (By.XPATH, "//app-card/div")
    cardFooter = (By.XPATH, "div/button")
    cardProduct = (By.XPATH, "div/h4/a")
    cardSelect = (By.XPATH, "div/button")
    def __init__(self,driver):
        self.driver = driver


        #product.find_element(By.XPATH, "div/h4/a").text

        #product.find_element(By.XPATH, "div/button").click()



    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getProduct(self):
        return self.driver.find_elements(*CheckOutPage.cardProduct)

    # def getCardSelect(self):
    #     #return self.driver.find_elements(*CheckOutPage.cardSelect).click()
    #     # return self.driver.find_elements(*CheckOutPage.cardSelect).click()
    #     # confirmPage = ConfirmPage(self.driver)
    #     # return confirmPage
    #     return self.driver.find_elements(*CheckOutPage.cardSelect).click()

    def getCardSelect(self):
        elements = self.driver.find_elements(*CheckOutPage.cardSelect)
        if elements:  # Check if the list is not empty
            elements[0].click()  # Click on the first available button
        else:
            print("No product selection buttons found!")