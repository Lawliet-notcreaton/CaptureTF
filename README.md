# CaptureTF
Продукт проекта по теме: "системы по захвату флага для информационной безопасности".


Форма для сдачи флагов: https://docs.google.com/forms/d/e/1FAIpQLSdajbW6Ej_4ERpDVjFin0zg3HbYcHlUT229rdWbvsXGfLxgLg/viewform?usp=sf_link


Вполнил Кулубаев У.С.



## SSTI

![SSTI cheatsheet workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/serverside.png?raw=true)

https://github.com/swisskyrepo/PayloadsAllTheThings

## Установка

### на телефон
1. Скачиваем termux
2. вводим команду
   ```

    pkg update && pkg upgrade

   ```
3. устанавливаем python
```
pkg install python
```

4. устанавливаем и активируем виртуальную среду
```
python -m venv venv
source venv/bin/activate
```
5. устанавливаем django
```
pip install django
```
6. запускаем локальный сервер
```
cd /CaptureTF
python manage.py runserver
```
7. исследуем, учимся, достигаем!
