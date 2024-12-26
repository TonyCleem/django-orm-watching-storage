# Пульт охраны банка #

Пульт охраны - веб-панель для управления и контроля доступа в хранилище.
Общее использование недоступно. Ключ к базе не распространяется. Если понравился проект можете использовать исходники.

---

## Функционал
- **storage_information_view.py** - просмотр хранилища
- **passcard_info_view.py** - просмотр персональных пропусков
- **active_passcards_view** - (_функция в разработке_)

## Требования
Для запуска бота на вашем компьютере или сервере необходимо:
 
* Python 3.7+
* Установленные зависимости из `requirements.txt`
---
## Установка и запуск
1. Склонируйте репозиторий:

```bash
git clone https://github.com/TonyCleem/django-orm-watching-storage
cd django-orm-watching-storage
```
2. Создайте виртуальное окружение:

```bash
python3 -m venv env
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Запустите Django
```
python manage.py runserver
```
После запуска перейдите по адресу `localhost:8000` для управления

---
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).