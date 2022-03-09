import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver_97.exe')
        print("Launching chrome browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\drivers\\geckodriver_89.exe')
        print("Launching firefox browser..........")
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Suma'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
