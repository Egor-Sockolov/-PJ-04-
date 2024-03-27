

# Итоговый проект по автоматизации тестирования:
Объект тестирования: [Ростелеком (https://b2c.passport.rt.ru/](https://b2c.passport.rt.ru/)
 

[Ссылка на чек-листы, тест-кейсы и баг-репорт](https://drive.google.com/drive/folders/1kaAGCM5k25-agXwEFsVbPp2YUdnFu2uE?usp=sharing)

[Ссылка на актуальные требования к сайту: https://docs.google.com/document/d/1qXyps0WQGLu2Xa7UXHRpIiGvV0sASdBEdotXxzl3orI/edit


**Техническое задание Заказчика:**

1. Протестировать [требования](https://lms.skillfactory.ru/assets/courseware/v1/f78e146f0eb3ace247a28b07e66467de/asset-v1:SkillFactory+INTQAP+2022+type@asset+block/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_SSO_%D0%B4%D0%BB%D1%8F_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_last.doc).
2. Разработать тест-кейсы (не менее 20). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). 
   Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформить свой 
   набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. 
   Во время обучения вы работали с разными сервисами и шаблонами, 
   используйте их для оформления тест-кейсов и обнаруженных дефектов. 
   Если дефекты не обнаружены, то подумайте и опишите 3 потенциально возможных дефекта 
   на данном ресурсе.

**Примененные методы при разработке проекта**

Для разработки тест-кейсов использованы методы "черного ящика", 
функционального тестирования, UX-тестирование. 
Разработка проекта автотестирования выполнена по паттерну PageObject. 
Для разработки автотестов применялись библиотеки pytest, pytest-selenium. 
Использовались фикстуры параметризации, явные и неявные ожидания драйвером, 
различные способы описания локаторов (СSS_SELECTOR, XPATH, ID, CLASS_NAME, 
NAME). 

Проект разработан для операционной системы Windows 10 Pro 
/ Google Chrome Версия 115.0.5790.170 (Официальная сборка), (64 бит).

Также использованы техники тест дизайна:
- разбиение на классы эквивалентности
- анализ граничных значений
- тестирование состояний и переходов


### Структура проекта

В корневом каталоге проекта содержатся:
`README.md` - содержит информацию о проекте и ссылки на документы 
([чек-листы, тест-кейсы и баг-репорт](https://drive.google.com/drive/folders/1kaAGCM5k25-agXwEFsVbPp2YUdnFu2uE?usp=sharing)), 
а также на актуальные [требования к сайту: https://b2c.passport.rt.ru/](https://docs.google.com/document/d/1qXyps0WQGLu2Xa7UXHRpIiGvV0sASdBEdotXxzl3orI/edit).

`requirements.txt` - необходимые установочные модули


### Папка `tests`: 
`test_negative_auth.py` - негативные тесты страницы авторизации

`test_negative_registration.py` - негативные тесты страницы регистрации

`test_reset_page.py` - тесты страницы восстановления пароля

`test_positive_auth_page.py` - позитивные тесты страницы авторизации

`test_positive_registration.py` - позитивные тесты страницы регистрации

### Директория `pages`: 

`locators.py` - локаторы XPath и CSS на web-элементы сайта

`auth_page.py` - функции-обёртки для локаторов используемых для страницы авторизации

`register_page.py` - функции-обёртки для локаторов используемых для страницы регистрации

`reset_page.py` - функции-обёртки для локаторов используемых для страницы восстановления

пароля

`base.py` - функции для применения к локаторам явных ожиданий, получения 
главной страницы сайта и пути текущей страницы


`config.py` - учетные данные, используемые в процессе теста
