import time

import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.confirmPage import confirmPage
from pageObjects.HomePage import HomePage
from utilities.baseClass import baseClass


class TestOne(baseClass):
    # here driver will be class variable so to access it , we need to put it as self.driver
    def test_e2e(self):
        # log = self.getLogger()
        homepage = HomePage(self.driver)  # object creation
        # coz i have created a constructor that takes driver as an argument in the page class
        checkoutpage = homepage.shopItems()
        # log.info("getting all cards info")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            # log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.checkoutButton().click()
        confirmpage = CheckoutPage.checkoutItems(self)
        # log.info("Entering country name as ind")
        time.sleep(5)
        confirmpage.countryNameField().send_keys("ind")
        time.sleep(10)
        self.verifyLinkPresence("India")
        confirmpage.selectCountry().click()
        confirmpage.checkBoxForAgreement().click()
        confirmpage.submitButton().click()
        text = confirmpage.successConfirmationText().text
        # log.info("Text received from application is " + text)
        assert ("Success! Thank you!" in text)

    @pytest.fixture(params=[("AB", "BC", "CD"), ("JK", "LM", "MN")])
    def getData(self, request):
        return request.param
