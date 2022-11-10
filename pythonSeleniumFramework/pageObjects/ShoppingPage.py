import self as self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver
    list_of_items = (By.XPATH, "//a[text()='Add to cart']")
    cart = (By.CSS_SELECTOR, "a[class='cart-contents']")
    cart_button = (By.XPATH, "(//a[text()='Add to cart'])[3]")

    def get_list_of_items(self):
        return self.driver.find_elements(*ShoppingPage.list_of_items)

    def get_cart(self):
        return self.driver.find_element(*ShoppingPage.cart)

    def get_cart_button(self):
        return self.driver.find_element(*ShoppingPage.cart_button)













    #
    # list_of_items = (By.XPATH, "//a[text()='Add to cart']")
    # symbol = (By.ID, "navigation-symbol-search")
    # symbol_lookup = (By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']")
    # side = (By.XPATH, "//button[@direction='buy']")
    # quantity = (By.XPATH, "//input[@type='number']")
    # review_order = (By.CSS_SELECTOR, "#review-order-button")
    # send_order = (By.CSS_SELECTOR, "#send-order-button")
    # notification = (By.XPATH, "//div[text()= 'Notifications']")
    # original_message = (By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")
    #
    # def get_list_of_items(self):
    #     return self.driver.find_elements(*ShoppingPage.list_of_items)
    #
    # def get_symbol(self):
    #     return self.driver.find_element(*ShoppingPage.symbol)
    #
    # def get_symbol_lookup(self):
    #     return self.driver.find_element(*ShoppingPage.symbol_lookup)
    #
    # def get_side(self):
    #     return self.driver.find_element(*ShoppingPage.side)
    #
    # def get_quantity(self):
    #     return self.driver.find_element(*ShoppingPage.quantity)
    #
    # def get_quantity_input(self):
    #     return self.driver.find_element(*ShoppingPage.quantity)
    #
    # def get_review_order(self):
    #     return self.driver.find_element(*ShoppingPage.review_order)
    #
    # def get_send_order(self):
    #     return self.driver.find_element(*ShoppingPage.send_order)
    #
    # def get_notification(self):
    #     return self.driver.find_element(*ShoppingPage.notification)
    #
    # def get_order_confirmation(self):
    #     original_confirmation = []
    #     original_message = [
    #         self.driver.find_element(*ShoppingPage.original_message).text]
    #     print(original_message)
    #     for records in original_message:
    #         original_confirmation.append(records)
    #     print(original_confirmation)
    #     assert original_message == original_confirmation
    #     return original_message

