from lib2to3.pgen2 import driver
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShoppingPage import ShoppingPage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self):
        shopping = ShoppingPage(self, driver)
        list_of_items = shopping.get_list_of_items()

        for item in list_of_items:
            item.click()
            if item == shopping.get_cart_button():
                break















#     list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
# for item in list_of_items:
#     item.click()
#     if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[3]"):
#         break
# sleep(1)
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='cart-contents']")).perform()
# sleep(1)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward']")).click().perform()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR, "input[name='coupon_code']").send_keys("Tojtech Automation")
# sleep(1)
# driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
# wait = WebDriverWait(driver, 5)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
# print(driver.find_element(By.XPATH, "//div[@role='alert']").text)
# driver.get("http://shopping.beeyor.com/checkout/")
# driver.find_element(By.ID, "billing_first_name").send_keys("Nini")
# driver.find_element(By.ID, "billing_last_name").send_keys("Smith")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_address_1']").send_keys("531 E 7th St")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_city']").send_keys("Brooklyn")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_postcode']").send_keys("11218")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_phone']").send_keys("9293388765")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_email']").send_keys("nini@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "textarea[name='order_comments']").send_keys("I appreciate all your hard work, and my pets love to play in the boxes you deliver.")
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[allow='payment *']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card number']").send_keys("4242424242424242")
# driver.switch_to.parent_frame()
# sleep(2)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='Secure expiration date input frame']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card expiration date']").send_keys("12/34")
# driver.switch_to.parent_frame()
# sleep(2)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='Secure CVC input frame']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']").send_keys("001")
# driver.switch_to.parent_frame()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "button[value='Place order']").click()
#
