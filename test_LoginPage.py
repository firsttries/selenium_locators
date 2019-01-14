from selenium.webdriver import Chrome
from Locators import Locator
import pytest

@pytest.fixture()
def test_enivironment():
    global driver
    driver = Chrome()
    driver.minimize_window()
    driver.get('https://sa-rc.litebox.ru/accounts/login/')
    yield
    driver.close()
    driver.quit()

def test_login(test_enivironment):
    driver.find_element_by_xpath(Locator.login_field).send_keys("testLogin@1")
    driver.find_element_by_xpath(Locator.pass_field).send_keys("testpass")
    driver.find_element_by_xpath(Locator.button_entrance).click()
    assert "+7 (495) 137 09 90" == driver.find_element_by_xpath(Locator.text_email).text

def test_demo(test_enivironment):
    driver.find_element_by_xpath(Locator.button_demo).click()
    assert "Добро пожаловать в ДЕМО-режим" == driver.title
    
def test_logo(test_enivironment):
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name(Locator.logo).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert "Автоматизация магазина - кассовая программа для розничной торговли, система учета продаж LiteBox" == driver.title

def test_bucket(test_enivironment):
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name(Locator.bucket).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert "Купить онлайн-кассу 54-ФЗ для ИП и ООО (УСН,ОСНО и ЕНВД) – доставка по Москве и всей России" == driver.title

def test_facebook(test_enivironment):
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name(Locator.fb).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert "Facebook" == driver.title

def test_vk(test_enivironment):
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name(Locator.vk).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert "LiteBox. Автоматизация торговли. ЕГАИС. 54-ФЗ | ВКонтакте" == driver.title

def test_youtube(test_enivironment):
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name(Locator.yt).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert "LiteBox - Автоматизация розничной торговли - YouTube" == driver.title

def test_not_send(test_enivironment):
    driver.find_element_by_link_text(Locator.link_not_send).click()
    assert "Не приходят email?" == driver.title

def test_support(test_enivironment):
    driver.find_element_by_link_text(Locator.link_support).click()
    assert "Support LiteBox" == driver.title

def test_link_registration(test_enivironment):
    driver.find_element_by_link_text(Locator.link_registration).click()
    assert "Регистрация" == driver.title

def test_link_password(test_enivironment):
    driver.find_element_by_link_text(Locator.link_forget_pass).click()
    assert "Сброс пароля" == driver.title

def test_link_tarif(test_enivironment):
    driver.find_element_by_link_text(Locator.link_tarif).click()
    assert "Тарифы Litebox" == driver.title

