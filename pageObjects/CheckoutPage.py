from selenium.webdriver.common.by import By

from pageObjects.confirmPage import confirmPage


class CheckoutPage:
    cardTitle = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutBtn)

    def checkoutItems(self):
        print("HI ")
        self.driver.find_element(*CheckoutPage.checkOut).click()
        print("HI BYE")
        print(self.driver)
        return confirmPage(self.driver)




