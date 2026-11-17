from selenium.webdriver.common.by import By
import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(LINK)
    #time.sleep(30)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(buttons) == 1, "Кнопка добавления в корзину не найдена на странице товара"
