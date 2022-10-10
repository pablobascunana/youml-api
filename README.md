# YouML Manager

## Dependencies

*  Python > 3.8

## Installation

- Create virtual environment

```shell
python -m venv <venv name>
```

- Install pipenv

```shell
pip install pipenv
```

- Install dependencies

```shell
pipenv install
```

- To set up database and user

```shell
python src/manage.py migrate
python src/manage.py createsuperuser
```

If you use PyCharm you have all available commands for this project inside **.run** folder

- To start server

```shell
python src/manage.py runserve 
```

- To run tests without coverage

```shell
pytest src/tests
```

- To run tests with coverage in console

```shell
pytest --cov-report term-missing --cov-config=.coveragerc --cov=src src/tests
```

- TO run tests with coverage in HTML files

```shell
pytest src/tests --cov=src --cov-config=.coveragerc --cov-report=html:.test-results
```