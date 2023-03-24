from selenium.webdriver.common.by import By


class confirmPage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    country = (By.ID, "country")
    indiaAsCountry = (By.LINK_TEXT, "India")
    checkBoxForAgriment = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitBtn = (By.CSS_SELECTOR, "[type='submit']")
    confirmationText = (By.CSS_SELECTOR, "[class*='alert-success']")

    def countryNameField(self):
        return self.driver.find_element(*confirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*confirmPage.indiaAsCountry)

    def checkBoxForAgreement(self):
        return self.driver.find_element(*confirmPage.checkBoxForAgriment)

    def submitButton(self):
        return self.driver.find_element(*confirmPage.submitBtn)

    def successConfirmationText(self):
        return self.driver.find_element(*confirmPage.confirmationText)
