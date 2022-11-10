from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("http://shopping.beeyor.com/shop/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(params=[{"username": "nataliya2022", "password": "Tojtech2022!"},
                        {"username": "somenegativevalue", "password": "123456"}])
def data_load(request):
    return request.param
