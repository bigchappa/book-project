# :poop: Интернет-магазин на Django
> Pet-проект. Создается в целях более лучшего изучения Python / Django:

## :triangular_ruler: Стек проекта: 
- Python 3.12 (Django)
- HTML5, CSS (Bootstrap 5)
- PostgreSQL

## :package: [Зависимости бекэнда](https://github.com/bigchappa/book-project/Pipfile.lock)

## :whale: Работа с Docker

- Собрать проект (prod.env или dev.env)
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```

- Удаление контейнеров

  ```
  $ docker-compose down -v
  ```

- Применить миграции базы данных

  ```
  $ docker-compose exec web python manage.py makemigrations
  $ docker-compose exec web python manage.py migrate
  ```

## :closed_lock_with_key: Настройка входа в админку

```
$ docker compose exec web python manage.py createsuperuser
```
  
## :camera: Скрины проекта
![Изображение №1]()
![Изображение №2]()
![Изображение №3]()
![Изображение №4]()
![Изображение №7]()
![Изображение №8]()
![Изображение №9]()



