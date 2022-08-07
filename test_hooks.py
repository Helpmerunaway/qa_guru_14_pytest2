import allure
import pytest


# название браузера пишется в тестах
# @pytest.fixture()
# def browser1(request: pytest.FixtureRequest):
#     browser = request.config.getoption("--browser")
#     if (browser == "chrome"):
#         pass
#     else:
#         pass
#     pass


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    pass


# параметризация при помощи хука, значение берем из функции браузер и передаем в тесты
# например:
# test_hooks.py::test_mobile_page[chrome]
def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)

# пример использования на реальном проекте
# def pytest_generate_tests(metafunc):
#     """
#     Parametrize web_driver fixture of browser names based on run options
#     """
#     if 'browser' in metafunc.fixturenames:
#         browsers = (
#             CHROME_AND_FIREFOX_PARAM
#             if marker_in_node_or_its_parent(INCLUDE_FIREFOX_MARK, metafunc.definition)
#             else ONLY_CHROME_PARAM
#         )
#         metafunc.parametrize('browser', browsers, scope='session')


def test_desktop_page(browser):
    pytest.fail("Some reason")


def test_mobile_page(browser):
    pass

@allure.title("Desktop Page")
def test_desktop_page2(browser):
    pytest.fail("Some reason")

@allure.title("Mobile Page")
def test_mobile_page2(browser):
    pass