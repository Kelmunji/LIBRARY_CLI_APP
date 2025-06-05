# Library CLI App

A simple Python CLI app to manage books, members, and rentals using SQLAlchemy ORM.

## Setup
- `pipenv install`
- `alembic init alembic`
- Add models to Alembic env.py
- `alembic revision --autogenerate -m "Initial schema"`
- `alembic upgrade head`

## Usage
- `python main.py list_books`
- `python main.py list_members`
- `python main.py list_rentals`# LIBRARY_CLI_APP
