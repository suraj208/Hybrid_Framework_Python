from selenium import webdriver
import pytest


driver = None

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',action="store",default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    #pytest --browser_name "firefox"
     # parameter which can be passed with pytest command
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    else:
        driver = webdriver.Chrome(options=options)
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.maximize_window()

    request.cls.driver = driver         ## request => to class which is using fixture
    yield
    driver.close()
