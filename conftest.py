import allure
import pytest




def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    parser.addoption(
        "--browser",
        choices=['chrome', 'firefox'],
        # default='chrome',
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config: pytest.Config):
    if config.getoption("--mobile-only") and config.getoption("--browser") == 'firefox':
        raise ValueError("Нет мобильных тестов на Firefox")



# хук выполняется после коллекта но перед стартом тестов,
# например создать директории или отправить информацию о старте

def pytest_sessionstart(session: pytest.Session):
    pass


# хук позволяет вмешиваться в тесты которые мы собрали
# можем пробежаться по всем коллект тестам и выбрать тесты с "мобайл" и запустить, а тесты
# и отсортировать тесты по названию например:
def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
    for item in items:
        if "mobile" not in item.name and config.getoption("--mobile-only"):
            item.add_marker(pytest.mark.skip(reason="Mobile tests only"))
    return items.sort(key=lambda x: x.name, reverse=True)


# фикстуры прошли, запускается сам тест
# редактирование названия функции в аллюре при помощи хука
def pytest_runtest_call(item: pytest.Item):
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())

    #yield

# хук для действия с невыбранными тестами (выбраны -k)
def pytest_deselected(items):
    pass


# хук на окончание сессии
def pytest_sessionfinish(session: pytest.Session):
    pass

# просмотр репорта после прогона тестов
def pytest_report_teststatus(report, config):
    pass

# мы хотим чтобы наш хук выполнился после например аллюра (для того чтобы вызвать хук вовремя)
@pytest.hookimpl(hookwrapper=False)
def pytest_sessionstart2(session: pytest.Session):
    pass

