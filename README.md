<br />
<p align="center">
  <a href="https://github.com/meowsl/ecosvet.git">
    <img src="/public/static/favicon.svg" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">#ЭКОСвет</h1>

  <p align="center">
    <br />
    <a href="https://ecology-svet.ru">MVP</a>
    ·
    <a href="https://www.figma.com/design/wiotFXVsLsShy6vIbojjG3/ЭКОСвет?node-id=0-1&t=N4YP2C0YOVa1EdyN-1">Макет</a>
    ·
    <a href="https://t.me/slay_meow">Капитан</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Содержание</h2></summary>
  <ol>
    <li>
      <a href="">Анализ проблемы</a>
    </li>
    <li>
      <a href="">Решение</a>
      <ul>
        <li><a href="">Описание</a></li>
        <li><a href="">Установка</a></li>
        <li><a href="">Запуск</a></li>
      </ul>
    </li>
  </ol>
</details>

## Анализ проблемы

**Формулировка:** Проблема данного кейса заключается в том, что отсутствует единая платформа, база данных, в которой бы хранились все мероприятия и которая бы была удобна для всех. <br><br>
**Конкуренты:** Изучив суть проблемы, были выявлены уже готовые решения, которые имеют ряд недостатков. Среди таких недостатков можно отметить не ориентированный на пользователя интерфейс, хранение устаревших данных, утрата актуализации платформы и т.д. Некоторые из них:
<ol> 
  <li>https://ecoportal.su/</li>
  <li>https://eco.fedcdo.ru/</li>
</ol>


## Решение

### Описание

<h5>Реализованная функциональность:</h5>
<ul>
  <li>Авторизация посредством Telegram/Rest Framework Auth;</li>
  <li>Динамический вывод контента;</li>
  <li>Обработка заявок на создание мероприятия в Django Admin;</li>
  <li>Интерактивная карта (Yandex Maps) для адресов;</li>
  <li>UX/UI</li>
</ul>

<h5>Особенность:</h5>
<ul>
  <li>Наличие широкой базы контента;</li>
  <li>Авторизация посредством социальной сети;</li>
  <li>Бонусная система на базе геймификации;</li>
  <li>Современный стэк технологий;</li>
  <li>Направленность на широкую аудиторию</li>
</ul>

<h5>Перспективы (не успели реализовать за сутки):</h5>
<ul>
  <li>Настройка собственного Telegram-бота с системой уведомлений;</li>
  <li>Настройка метрики для начисления опыта пользователям;</li>
  <li>Уровневная система, открывающая новые возможности</li>
</ul>

<h5>Стэк технологий:</h5>
<ul>
  <li>Python 3.10.0, Django 3.2, Django Rest Framework 3.13</li>
  <li>Vue 3, Quasar CLI 2.6.0, ESlint 8.10</li>
  <li>PostgreSQL, SQLite 3</li>
  <li>Poetry, Yarn, Makefile</li>
  <li>Git, Docker, Docker Compose</li>
  <li>NVM, Pyenv</li>
  <li>CRUD, БЭМ</li>
</ul>

### Установка

1. Клонируем репозиторий
   ```
   git clone https://github.com/meowsl/ecosvet.git
   ```
2. Установка бэкенда:
   2.1. Poetry
     ```
       poetry install --no-root
     ```
   2.2. Pip
     ```
     pip install -r requirements.txt
     ```
3. Установка фронтенд пакетов
   ```
   yarn install
   ```
4. Постустановка
   ```
   poetry run task migrate
   или
   python ./server/manage.py migrate --noinput 
   ```


### Запуск
Бэкенд:
```
poetry run task manage runserver
или
python ./server/manage.py runserver
```
Фронтенд:
```
yarn quasar dev
```

P.s. Рекомендуем использовать наш стэк технологий и тогда все запустится без проблем:
```
make install
```
```
make run
```
