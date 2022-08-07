import time

import pytest


# при параллельном запуске session scope фикстура будет вызвана много раз
@pytest.fixture(scope="session", autouse=True)
def session_scoped_fixture():
    pass


# параметризация на 20 тестов
# [gw0] [100%] PASSED test_xdist.py::test_many_params[10]
@pytest.mark.parametrize("param", range(20))
def test_many_params(param, session_scoped_fixture):
    time.sleep(1)