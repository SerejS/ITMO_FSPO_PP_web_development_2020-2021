# ITMO_FSPO_PP_web_development_2020-2021
Репозиторий для реализации дистанционного обучения по дисциплине "УП.11.01"

[Учебный журнал](https://docs.google.com/spreadsheets/d/1w43P8IImUzLnYtFtFlwGiW9L2ksz6EDoyAX_GRD8utM/edit#gid=0) по дисциплине. Тут доступна информация о сроках сдачи работ, о текущей успеваемости студентов и описаны все материалы необходимые для реализации курса.

## Инструкции
Дополнительные материалы делятся на 3 категории:

1. Для тех, кто считает, что имеет недостаточно базовых знаний об информатике, веб-разработке и сетях (обзначается **(+)**).
2. Для тех, кто считает, что имеет базовые знания  (обзначается **(++)**).
3. Для тех, кто хочет поглубже изучить материал  (обзначается **(+++)**).

### Лекция 1.1 - Концепции разработки веб сервисов.
Презентация с лекции [тут](https://drive.google.com/file/d/1uZMyzGn_42krfuEdR-pLmcrb2LGqYNmx/view?usp=sharing).

Допонительные материалы:

1. [Иерархия компьютерных информационных систем для разработки сайта](https://habr.com/ru/post/513486/) **(+)**
2. [Топ-5 наиболее популярных CMS: какую выбрать?](https://habr.com/ru/post/151879/) **(++)**
3. [Веб-фреймворки: введение для новичков (классификация фреймворков)](https://tproger.ru/translations/web-frameworks-how-to-get-started/) **(++)**
4. [Чем отличаются фронтенд- и бэкенд-разработка](https://techrocks.ru/2020/07/01/front-end-vs-back-end-development/) **(+)**
5. [Что такое MVC: базовые концепции и пример приложения](https://skillbox.ru/media/code/chto_takoe_mvc_bazovye_kontseptsii_i_primer_prilozheniya/) **(++)**

### Практическая часть 1.1

Погуглить и описать **своими словами**, что такое frontend и backend. Привести примеры frontend и backend фреймворков. Описать отличия.

Отчет о практической части содержит текстовый файл с вашим текстом работы и отправляется пул реквестом в этот репозиторий в папку lection_1_pr_1.1 **(Пример  students/Y2331/Petrov_Vasya/lection_1_pr_1.1 )**. Шаблон названия пул реквеста "ИТМО ФСПО Номер_группы Практическая работа ФИО". Пример: "ИТМО ФСПО К3340 Практическая работа №1 Филимонов Филипп". 

### Практическая работа 1.2
**Дедлайн: 9.03.21 10:00**

Цель работы: дать краткое представление о работе Django **WEB** фреймворка.<br>
1. Необходимо установить Django Web framework. [Инструкция по установке](https://drive.google.com/file/d/1fsNaCm2MCxVletRLdGzVrd6-lPePn2Xh/view). Если у Вас нет PyCharm Professional, пропустите пункт 8. 
Формат именований блоков проекта:
- Формат имени Django-проекта: “django_project_фамилия”.
- Формат имени Django-приложения: “project_first_app”.

П.С. Если Вы работаете на компьютерах ФСПО и у Вас появляется ошибка импорта модуля sqlite3, решение [тут](https://stackoverflow.com/questions/54876404/unable-to-import-sqlite3-using-anaconda-python) в первом ответе.

2. Необходимо выполнить все задания с пометкой **практическая работа** из [практической работы №1](https://docs.google.com/document/d/1zHvKAh_CDcSnpFPgtNQq7JulRoBTiY4OdMlRth-Rjuc/edit?usp=sharing).<br>
Полученную программу загрузить в папку этого репозитория **sutdents/группа/фамилия_имя/practical_works/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

Для удобства навигации по практическим работам необходимо открыть меню оглавления (см. скриншоты ниже)<br><br>
![Image alt](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021/raw/master/static/images/folders_1.png "Открытие оглавления")<br><br>
![Image alt](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021/raw/master/static/images/folders_2.png)<br>

### Лекция 1.2 - Компоненты клиент-серверного взаимодействия.
Презентация лекции [тут](https://drive.google.com/file/d/1Jp_7c5GcK8TeLii2yEDuSmjLyXIlGQs1/view?usp=sharing).

Дополнительные материалы:

1. [Сетевая модель OSI](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_OSI) **(+)**
2. [Адресация в сетях](https://support.microsoft.com/ru-ru/help/164015/understanding-tcp-ip-addressing-and-subnetting-basics) **(+)**
3. [TCP vs UDP](https://habr.com/ru/company/oleg-bunin/blog/461829/) **(+++)**

### Практическая работа №1.3

Цель работы: дать подробное представление о реализации CRUD(Create, read, update and delete) интерфейсов средствами Django **WEB** фреймворка.<br>
Необходимо выполнить все задлания с пометкой **практическая работа** из [практической работы №2](https://docs.google.com/document/d/1koLV9iGXJfL2yh88InKo4AVXxWqMIJOqmzT4XFYlWuU/edit?usp=sharing).<br>
Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

### Практическая работа №1.4

Необходимо выполнить все задлания с пометкой **практическая работа** из [практической работы №3](https://docs.google.com/document/d/1kQ36RlRtxqpjtUtfr-WCWkuJ1SYvSG4220Ops2X0viw/edit?usp=sharing
). <br>
Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

### Полезные материалы

[Фундаментально](https://www.youtube.com/playlist?list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX) - плейлист уроков по джанго для тех кто хочет **фундаментально** изучить, как работает джанго веб фремйворк и заниматься этим в будущем.

[Базово](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqP4S95brtPHZ5fTCxilgei) - плейлист, который позволит **быстро** понять, как и что работает и **сделать лабу**.

# Лабораторная работа


**Есть два варианта сделать работу:**<br>
**- Простой: Выполнить ЛР 1.1 - сделать простое веб-приложение без отдельного клентского приложения (Django WEB framework) (оценки 3-4-5(на 5 нужгно будет сделать ооочень крутую работу(5 получить почти невозможно))** (Дедлайн: иначально был 4.05.2021 -> продлен до **18**.05.2021) <br> 
**- Сложный: Выполнить ЛР 1.2 - 1.3 - сделать более сложное веб-приложение состоящее из серверной части django rest framework и клиентской части на vue.js (оценки 4-5(на 4 нужно сделать совсем просто, на 5 нормально и выше) + просроченный дедлайны по предыддущим работам будут сброщены)** (Дедлайн: иначально был 4.05.2021 -> продлен до 01.06.2021) <br>

# Лабораторная работа №1.1. Реализация web-приложения средствами Django WEB framework (Будет дополняться)
**Дедлайн: 11.05.21 10:00**

Реализация веб-приложения на джанго в соответствии с вариантом из практики с Татьяной Николаевной. Вам нунжно не просто сделать CRUD(Create Read Update Delete) интерфейсы для БД, а сделать небольшой сервис, который решает какую-то проблему.

Обращаем внимание, что **доступна возможность предложить свой индивидуальный вариант** и делать работу по нему. <br>

Этапы работы:
1) Сделать **новый** проект. Шаблон названия проекта *название системы_project*. Шаблон названия приложения *суть приложения_app*.
2) Реализовать модель данных. Не забыть про ограничения целосности и связи между таблицами. Использовать одного пользователя (расширить стандратного пользователя им).
3) Описать ваш проект в техническом задании. Утвердить список интерфейсов в лабораторной работе с преподавателем.
    Список страниц в ТЗ:
    - Обзщее описание проекта.
    - Описание таблиц модели данных + модель данных в любой нотации.
    - Список интерфейсов с описанием входных и выходных данных.
Реализовать ТЗ в Read the Docs или MkDocs (Инструкции по работе с mkdocs - пункт 3 [из практической работы №3.2](https://docs.google.com/document/d/1rIfREFvCB4pp8uF990Tz3PLXRJ5u_w-Y3vLxfXWKoxg/edit?usp=sharing)).
5) Реализовать интерфейсы (описание будет дополненно).
    Минимальное функциональное наполнение интерфейсов:
    - Использовать UI библиотеку (настройка форм c bootstrap - https://django.fun/tutorials/django-i-formy-bootstrap-4/)
    - Реализовать разные интерфейсы для пользователей разных групп (https://djbook.ru/rel1.9/topics/auth.html#authentication-in-web-requests)
    - Реализовать меню (меню с бутсрап - https://www.youtube.com/watch?v=HEPTgggsRgY)
    - Реализвать пагинацию страниц (так себе вариант - https://evileg.com/ru/post/10/ , отличный вариант - https://evileg.com/ru/post/237/)
    - Внедрить поиск по объектам, с которыми настроена пагинация (https://evileg.com/ru/post/21/)
6) Реализовать документацию, описывающую работу всех используемых endpoint-ов из пункта 3 и 4 средствами Read the Docs или MkDocs.<br><br> По пункту 3: Показать модель БД (изображение), код создания модели данных с комментариями. <br> По пункту 4: Описать все url-адреса и функционал, который они реализуют. <br>  <br>
Полезные материалы:
    - Пункт 3 [из практической работы №3.2](https://docs.google.com/document/d/1rIfREFvCB4pp8uF990Tz3PLXRJ5u_w-Y3vLxfXWKoxg/edit?usp=sharing)

# Лабораторная работа 1.2 (Сложный путь для тех, кто хочет стать веб-разработчиком) (получаете 4 или 5 за курс - 100% (при выполнении всех предыдущих работ) + просроченный дедлайны по предыддущим работам будут сброщены). Реализация серверной части на django rest. Документирование API.

Цель работы: овладеть практическими навыками реализации серверной части (backend) приложений средствами Django REST framework.

## Практическая работа №1.2.1 (необязательно к выполнению)

Цель работы: получить представление об использовании возмжностей работы контроллеров и серриализаторов в Django Rest Framework.
Необходимо выполнить все задания с пометкой **"Практическое задание** [из практической работы №3.2] (https://docs.google.com/document/d/1PkpwxCUYQ2_Pi8Fpcgno6te3oCQHZfkh03Zxt6DhHSw/edit?usp=sharing). Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_drf_project**. 
Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

## Практическая работа №1.2.2 (необязательно к выполнению)

Цель работы: овладеть навыками написания документации к API.<br>
Необходимо выполнить все задания с пометкой **"Практическое задание"** [из практической работы №3.2](https://docs.google.com/document/d/1rIfREFvCB4pp8uF990Tz3PLXRJ5u_w-Y3vLxfXWKoxg/edit?usp=sharing).<br> Результаты практики загружаются в репозиторий вместе с лабораторной работой.

## Лабораторная часть

Срок сдачи ****

Реализация серверной части приложения средствами django и djangorestframework в соответствии с заданием из [текста работы](
https://drive.google.com/file/d/1QxQo5jln6soFUj6EmOVEo1yauCo375PP/view?usp=sharing).<br>

Порядок выполнения работы:<br>
1.	Выполнить [практическую работу 3.1](https://docs.google.com/document/d/1PkpwxCUYQ2_Pi8Fpcgno6te3oCQHZfkh03Zxt6DhHSw/edit)<br><br>
2.	Выбрать вариант или предложить свой, есть 4 способа:<br>
2.1.	Предложить свой вариант.<br>
2.2.	Использовать вариант из дисциплины из дисциплины Татьяны Николаева.<br>
По любому из способов функционал нужно согласовать с преподавателем или ментором. В лабораторной работе №4 необходимо будет реализовать клиентскую часть(фронтенд) по этому же варианту.<br><br>
3.	Реализовать модель базы данных средствами DjangoORM (согласовать с преподавателем на консультации).<br>
При необходимости, студент может согласовать модель базы данных с преподавателем и только потом приступить к описанию модели средствами Django ORM<br>
Полезные материалы:<br>
    - [Создание модели данных в Django ORM](https://www.youtube.com/watch?v=LZyk9p0tKXc) (Видео)<br><br>
4.	Реализовать логику работу API средствами Django REST Framework (используя методы сериализации).<br>
Полезные материалы:<br>
    - Пункты 4, 5, 6 в [Практической работе 3.1](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021)<br>
    - [DJANGO API VIEWS, GENERICS, FILTER](https://youtu.be/AHnBL9x6-rs) (Видео)<br>
    - [JSON. Сериализация данных. Пишем свой сериализатор. Разбираем Django REST Framework Serializers](https://youtu.be/sxdPf3z6Uw8) (Видео)<br>
    - [Работа с Django ORM](https://youtu.be/HhrPbmHbDPU) (Видео)<br><br>
5.	Подключить регистрацию / авторизацию по токенам / вывод информации о текущем пользователе средствами Djoser.<br>
Полезные материалы:<br>
    - Djoser ([DRF + Djoser часть 1. Регистрация, авторизация по токенам, получение и изменение данных пользователя](https://youtu.be/NT-cI6rJl5Q)) (Видео)<br><br>
6.	Выполнить практическую работу 3.2 по оформлению документации (в процессе разработки)<br><br>
7.	Реализовать документацию, описывающую работу всех используемых endpoint-ов из пункта 3 и 4 средствами Read the Docs или MkDocs.<br><br> По пункту 3: Показать модель БД (изображение), код создания модели данных с комментариями. <br> По пункту 4: Описать все url-адреса и функционал, который они реализуют. <br>  <br>
Полезные материалы:
    - Пункт 3 [из практической работы №3.2](https://docs.google.com/document/d/1rIfREFvCB4pp8uF990Tz3PLXRJ5u_w-Y3vLxfXWKoxg/edit?usp=sharing)

Работа выполняется индивидуально.<br>
Код практический и лабораторной части должен быть загружен в репозиторий курса, в соответствии с инструкциями тут.<br>
Работу необходимо защитить на консультации или прислать видео с описанием проделанной работы.<br>

## Сдача работы №3

Работа выполняется индивидуально.<br>

### Этап 1
Полученную программу залить в папку этого репозитория **sutdents/группа/laboratory_works/фамилия_имя/laboratiry_work_3**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

### Этап 2
Работу необходимо защитить лично или прислать видео с описанием проделанной работы.

## Дополнительный контент для тех, кто хочет лучше изучить DRF и работать с ним в будущем::

Лекция 1

Содержание:

- REST и альтернативы. ([Лекция 06.11.2020 / Время 00:00 - 00:35](https://youtu.be/PI-FPq3zhpc))<br>
- Django rest framework. ([Лекция 06.11.2020 / Время 00:35 - 02:20](https://youtu.be/PI-FPq3zhpc))<br>
- Подробно о формате json. ([Лекция 06.11.2020 / Время 02:20 - 03:15](https://youtu.be/PI-FPq3zhpc))<br>
- Сериализация. ([Видео по сериализации от Давида](https://www.youtube.com/watch?v=sxdPf3z6Uw8&feature=youtu.be))<br>

Лекция 2

- Документирование апи
- Виды авторизации (сессии, токены)
- JWT + Использование JWT в Django
- Djoser ([DRF + Djoser часть 1. Регистрация, авторизация по токенам, получение и изменение данных пользователя](https://youtu.be/NT-cI6rJl5Q))

1) [простой курс](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqP9PqPU3LA7mX2KJVyLhC_) - плейлист уроков по джанго для тех, кто хочет **быстро** изучить, как работает работает Django rest framework в связке с vue.js. (Примечание. В уроке 4 изменился путь для получения токена авторизации (см. официальную докумекнтацию Djoser https://djoser.readthedocs.io/en/latest/getting_started.html))
1) [более подробный курс, чем в пункте 1](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C)

# Лабораторная работа 1.3.(Сложный путь для тех, кто хочет стать веб-разработчиком) (получаете 5 за курс - 100%). Реализация клиентской части средствами Vue.js.

## Практическая работа №1.3.1 (необязательно к выполнению)

Цель работы: Ознакомится с базорвыми конструкциями JavaScript.
[Текст "Практической работы №4.1](https://docs.google.com/document/d/1lurVq_ddbKQ-rORvxF3T9PlPPy-sOgHwFazCI0yEqYY/edit?usp=sharing).

## Практическая работа №1.3.2 (необязательно к выполнению)

Цель работы: получить представление о работе Vue.js.
[Текст "Практической работы №4.2](https://docs.google.com/document/d/1ZURAlewVuJFSX4YjjB-BvVsVwfF5IbXFH8zj2g8CgPY/edit?usp=sharing).

## Практическая работа №1.3.3 (необязательно к выполнению)

Цель работы: получить практические навыки настройки CORS (Cross-origin resource sharing).
[Текст "Практической работы №4.3](https://docs.google.com/document/d/1diaE5abmxSYEpLCwAp-or9c_h11-wR8ZSGQl3_b0nsc/edit?usp=sharing).

## Лабораторная часть

Реализация клиентской части приложения средствами vue.js, в соответствии с [текстом работы](
https://drive.google.com/file/d/1q9KcLhl2uKuK92aFbpKiOZ1WUwbASTqL/view?usp=sharing).<br>

Порядок выполнения работы:<br>
1.	Выполнить практическую работу 4.1 Базовые конструкции языка JavaScript). (https://docs.google.com/document/d/1lurVq_ddbKQ-rORvxF3T9PlPPy-sOgHwFazCI0yEqYY/edit?usp=sharing)
2.	Выполнить практическую работу 4.2. Работа с Vue.JS. (https://docs.google.com/document/d/1ZURAlewVuJFSX4YjjB-BvVsVwfF5IbXFH8zj2g8CgPY/edit?usp=sharing)
3.	Настроить для серверной части, реализованной в лабораторной работе №3 CORS (Cross-origin resource sharing) в соответствии с Практической работой 4.3 (будет выложена 19.12.2020)
4.	Утвердить с одним из преподавателей список интерфейсов для взаимодействия с серверной частью.
5.	Реализовать интерфейсы авторизации, регистрации и изменения учётных данных и настроить взаимодействие с серверной частью.
Полезные материалы:<br>
    - Настройка авторизации средствмаи Vue.js и Django REST framework (DjangoSchool) ([ссылка](https://youtu.be/0VuOGByhiKU?list=PLF-NY6ldwAWqP9PqPU3LA7mX2KJVyLhC_))<br>
6.	Реализовать клиентские интерфейсы и настроить взаимодействие с серверной частью.
Полезные материалы:<br>
    - Пункты 4.2, 4.3, 4.5 в [Практической работе 4.2](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021)<br>
    - Уроки 6, 7  и 10-13 из данного плейтиста (DjangoSchool) ([ссылка](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqP9PqPU3LA7mX2KJVyLhC_))
7.	Подключить vuetify.
Полезные материалы:<br>
    - Пункт 3.1 в [Практической работе 4.2](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021)<br>
8.	Реализовать документацию, описывающую работу разработанных интерфейсов средствами MkDocs.

## Сдача работы №4

Работа выполняется индивидуально.<br>

### Этап 1
Полученную программу залить в папку этого репозитория **sutdents/группа/laboratory_works/фамилия_имя/laboratiry_work_4**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

### Этап 2
Работу необходимо защитить лично или прислать видео с описанием проделанной работы.

## Дополнительный контент для тех, кто хочет лучше изучить DRF и работать с ним в будущем:

### Лекция 4.1 (Основы создания клиентских web-приложений)

- Отличие многостраничного приложения от SPA [Презентация с лекции(.ppt)](https://drive.google.com/file/d/1aUwwy7xKJ32J9rXumK-xcI_ttWm1vcSx/view?usp=sharing) | [Лекция 20.11.2020 / Время 00:00 - 00:16](https://youtu.be/oihJcLNoewo) (Видео)<br>
- Angular vs. Vue vs. React [Презентация с лекции(.ppt)](https://drive.google.com/file/d/1bNEVcfHRo0T9n1IDYwnn0YIPEGUIO51a/view?usp=sharing) | [Лекция 20.11.2020 / Время 00:16 - 00:58](https://youtu.be/oihJcLNoewo) (Видео)<br>
- Компонентный подход + как работает роутинг на фронтенде [Лекция 20.11.2020 / Время 00:58 - 01:45](https://youtu.be/oihJcLNoewo) (Видео)<br>

### Лекция 4.2 (Основы работы с JS)
1. Типы данных (number, infinity, NaN, undefinded, bigint, string, bool, null, object) + Переменные (var, let, const) + Функции (анонимнные, lambda) + Циклы (foreach, for, while) + Работа с массивами (filter, sort, map, forEach) [Лекция 04.12.2020 / Время 00:00 - 00:44](https://youtu.be/Lc0gO-kf38M) (Видео)<br>
2. Работа с событиями (load, DOMContentLoaded, click, change, submit, reset), работа с DOM-деревом (кнопки, формы),
работа с DOM-хранилищами (localStorage, sessionStorage) [Лекция 04.12.2020 / Время 00:44 - 02:04](https://youtu.be/Lc0gO-kf38M) (Видео)<br>

### Лекция 4.2 (Основы работы с Vue.js)
https://youtu.be/ckzWDhn8ScQ

## Сдача работ

Для сдачи работы в связи с переходом на дистанционную форму обучения введены дополднительные правила игры.

Все отчеты сохраняются в **pdf** (документы и презентации).

Все студенческие работы хранятся в папке **Students**
Для сдачи работы необходимо:

1. Зарегистрироваться на Git.
2. Сделать форк репозитория с заданиями в свой аккаунт (на странице https://github.com/TonikX/ITMO_FSPO_PP_web_development_2020-2021 кнопка fork справа, сверху).
3. Установить Git на компьютер (https://git-scm.com/download/win).
4. Открыть папку, где хранятся Ваши проекты. В контекстом меню нажать "Open Git Bash here". Склонировать форкнутый репозиторий на комьютер (git clone https://github.com/ваш аккаунт/ITMO_FSPO_PP_web_development_2020-2021).
5. В файловой системе Вашего компрьютера в склонированном репозитории создать в папке students/группа Вашу личную папку в формате Фамилия_Имя латиницей (Пример **sutdents/k3340/Petrov_Vasya**).
6. В личной папке сделать подпапку с текущей работой в формате lr_номер (Пример **sutdents/k3340/Petrov_Vasya/Lr1**).
7. Записать в папку отчетные материалы.
8. Сделать коммит, описать его адекватно (Пример "был добавлен файл перезентация_петров.pdf"). Набрать команлы git add и git commit -m "название комита".
9. Сделать push в Ваш форкнутый репозиторий (git push).
10. Сделать пул-реквест в репозиторий преподавателя из вашего форкнутого, описать его. Структура заголовка пулреквеста: **Фамилия_Имя-Работа_Номер** (Пример: Петров_Василий-Лабораторная_работа_1).

Пользуйтесь [этой](https://vk.com/@efimchik_post_edu-tfm-2019-1) инструкцией, у нас нет веток с заданиями, как тут, но Вам поможет.
Все работы сдаются средствами создания Pull Requests в папку students в этом репозитории.

Еще один мануал о том, как сделать Pull Request описано [тут](https://rustycrate.ru/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%B0/2016/03/07/contributing.html).

