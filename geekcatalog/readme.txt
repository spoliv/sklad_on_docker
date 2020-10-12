1. Установить docker и docker-compose.

2. В домашний каталог /home/user поместить папку geekcatalog, файлы .env.dev и docker-compose.yml.

3. В файле .env.dev вместо secret_key_of_django, name_of_DB, user, password_of_DB подставить соответствующие значения.

4. В файле docker-compose.yml вместо name_of_DB, user, password_of_DB подставить соответствующие значения.

5. Соберем новый образ и запустим два контейнера: 

$ docker-compose up -d --build

6. Запустим миграцию:

$ docker-compose exec web python manage.py migrate --noinput

7. Перейдем на страницу http://localhost:8000/

8. В дальнейшем для нового запуска контейнера выполняем команду:

$ docker-compose up -d

 и в браузере переходим на страницу http://localhost:8000/