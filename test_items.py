from selenium.webdriver.common.by import By
import time

link = "https://www.youtube.com/"

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)

    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"),\
        "There is no ADD TO BASKET button"