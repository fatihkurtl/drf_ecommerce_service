# DRF E-Commerce Service

## About the project

This project aims to create e-commerce service with Django Rest Framework. Thanks to this service, users can view products, add to cart, order and pay. In addition, users can add their own products and offer them for sale.

## Setup

To run this project, follow these steps:

- Clone or download the project to your computer.
- Go to project directory and create virtual environment. For example: `python -m venv venv`
- Activate the virtual environment. For example: `venv\Scripts\activate`
- Install required packages. For example: `pip install -r requirements.txt`
- Make database migrations. For example: `python manage.py makemigrations` and `python manage.py migrate`
- Create superuser. For example: `python manage.py createsuperuser`
- Run the project. For example: `python manage.py runserver`

## Use

After running the project you can use the following API endpoints:

- `/api/ecommerce/`: Lists all products or adds a new product.
- `/api/ecommerce/<int:pk>/`: Shows or updates or deletes the details of a particular product.
- `/api/ecommerce/category/`: Lists all categories or adds a new category.
- `/api/ecommerce/category/<int:pk>/`: Shows or updates or deletes the details of a particular category.
- `/api/ecommerce/cart/`: Lists the user's cart or adds a new product.
- `/api/ecommerce/cart/<int:pk>/`: Shows or updates or deletes the details of a particular product in the cart.
- `/api/ecommerce/order/`: Lists the user's orders or creates a new order.
- `/api/ecommerce/order/<int:pk>/`: Shows or updates or deletes the details of a particular order.
- `/api/ecommerce/payment/`: Lists the user's payments or makes a new payment.
- `/api/ecommerce/payment/<int:pk>/`: Shows or updates or deletes the details of a particular payment.

## Tests

You can use the following command to run the tests in the project:

`python manage.py test`

## Technologies

This project uses the following technologies:

- Python
- Django
- Django Rest Framework
- SQLite

## Contributors

Contributors to this project include:

- Fatih Kurt
- ...

## Licence

This project is licensed under the MIT license. For license [here](https://medium.com/@havvanurselamet/github-profi%CC%87li%CC%87-i%CC%87%C3%A7i%CC%87n-read-me-file-olu You can click %C5%9Fturma-and-d%C3%BCzenleme-53470377bbc0).
