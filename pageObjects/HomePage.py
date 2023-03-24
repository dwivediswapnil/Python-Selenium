from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")  # class variable
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    # def shopItems(self):
    #     return self.driver.find_element(*homePage.shop)
    #         "*homePage.shop" is used to use it as a tuple and deserialize it like
    #          driver.find_element_by_css_Selector("a[href*='shop']"), If i do not put star , then it will
    #           place it like that only.
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
