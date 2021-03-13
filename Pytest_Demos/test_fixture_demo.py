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

@pytest.mark.orange
def test_title_name(test_login):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    if driver.title =="OrangeHRM":
        assert True
    else:
        assert False

@pytest.mark.facebook
def test_facebook(test_login):
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)

@pytest.mark.flipkart
def test_flipkart(test_login):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("Flipkar is ready")

'''def pytest_configure(config):
    config._metadata["Project Name"]="Fixture Demo "
    config._metadata["module Name"] = "test_fixture_demo "
    config._metadata["Name of tester"]="Vishnu"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Packages",None)
    metadata.pop("Platform",None)
    metadata.pop("Plugins",None)'''

