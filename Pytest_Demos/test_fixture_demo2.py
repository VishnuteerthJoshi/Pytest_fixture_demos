from selenium import webdriver
import pytest
@pytest.fixture()
def test_setup():
    print("This method is executed first:")

def test_method1(test_setup):
    print("This is method1")

def test_method2(test_setup):
    print("This is second method:")
