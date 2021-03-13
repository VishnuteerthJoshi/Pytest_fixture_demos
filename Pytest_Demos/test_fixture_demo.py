from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
import time
import logging

#global driver
@pytest.fixture()
def test_login():
    global driver
    driver=webdriver.Chrome()
    print("This is executed first :")
    yield
    driver.close()


def test_title_name(test_login):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    if driver.title =="OrangeHRM":
        assert True
    else:
        assert False

def test_facebook(test_login):
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)

def test_flipkart(test_login):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("Flipkar is ready")



