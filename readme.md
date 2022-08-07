
- Хуки pytest - специальные функции которые выполняются в разные моменты жизни теста
    - Примерное дерево хуков - https://github.com/pytest-dev/pytest/issues/3261#issuecomment-369740536
    - pytest_addoptions - добавляем новые опции
    - pytest_configure - меняем что-нибудь в конфигурации
    - pytest_sessionstart - делаем что-нибудь перед стартом всех тестов
    - pytest_generate_tests - изменяем параметризацию тестов
    - pytest_collection_modifyitems - редактируем собранные тесты
    - pytest_runtestloop - хули во время выполнения тестов
    - pytest_sessionfinish - все тесты завершились

- xdist - плагин для параллелизации тестов 
(как правильно работать с конкурентностью ресурсов)
  - аргумент -n - нампроцессес (сколько параллелей нужно, можно задать -n auto)
  - фикстуры xdist
  - как себя ведут session scope фикстуры?