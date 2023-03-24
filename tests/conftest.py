import pytest
from selenium import webdriver


# This code is known as hook
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# here running the cmd "py.test --browser_name chrome" from cmd prompt will work for the run.
@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\swapn\\PycharmProjects\\pythonProject\\PythonSelfFramework\\chromedriver.exe")
        driver.get("https://qaclickacademy.github.io/protocommerce")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\swapn\\PycharmProjects\\pythonProject\\PythonSelfFramework\\geckodriver.exe")
        print("firefox")
    elif browser_name == " IE":
        print("IE")

    # now the driver declared here will be sent to class object (ex: test_e2e driver object)
    request.cls.driver = driver  # ** imp step
    # yield
    # driver.close()
