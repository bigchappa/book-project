# Интернет-магазин на Django
> Pet-проект. Создается в целях более лучшего изучения Python / Django:

## :triangular_ruler: Стек проекта: 
- Python 3.12 (Django)
- HTML5, CSS (Bootstrap 5)
- PostgreSQL

## :package: [Зависимости бекэнда]([https://github.com/bigchappa/book-project/Pipfile.lock](https://github.com/bigchappa/book-project/blob/master/Pipfile.lock))

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
![Image](https://github.com/user-attachments/assets/8ca04412-6366-4ee9-b5c8-462f7c346f47)
![Image](https://github.com/user-attachments/assets/c17616de-929a-438a-b149-84f795e1ecc8)
![Image](https://github.com/user-attachments/assets/52950cf9-8a59-4604-82f8-7da643812624)
![Image](https://github.com/user-attachments/assets/08c7ae9b-9989-4f21-ae95-938139678026)
![Image](https://github.com/user-attachments/assets/c248f187-c42f-44a0-bf54-109da3a28ba1)
![Image](https://github.com/user-attachments/assets/b91b878b-ce7c-4b52-b728-6c1309ce9b49)
![Image](https://github.com/user-attachments/assets/d594ac45-1841-4c9f-aca8-ef2481e8830b)
![Image](https://github.com/user-attachments/assets/5df904f1-b309-4fec-bcbc-8ed05161f252)
![Image](https://github.com/user-attachments/assets/7a5fc0f6-43cc-4041-903c-abdd0597a7a7)







