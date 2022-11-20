# YouML Manager

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=coverage)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=youml-manager)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=youml-manager&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=youml-manager)
<br />
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e58e5d43af804c68a911b1cf7e44d789)](https://www.codacy.com/gh/pablobascunana/youml-manager/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pablobascunana/youml-manager&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/e58e5d43af804c68a911b1cf7e44d789)](https://www.codacy.com/gh/pablobascunana/youml-manager/dashboard?utm_source=github.com&utm_medium=referral&utm_content=pablobascunana/youml-manager&utm_campaign=Badge_Coverage)


## Dependencies

*  Python > 3.8

## Installation

* Create virtual environment

```shell
python -m venv <venv name>
```

* Install pipenv

```shell
pip install pipenv
```

* Install dependencies

```shell
pipenv install
```

* To set up database and user

```shell
python src/manage.py migrate
python src/manage.py createsuperuser
```

If you use PyCharm you have all available commands for this project inside **.run** folder

* To start server

```shell
python src/manage.py runserve
```

* To run tests without coverage

```shell
pytest src/tests
```

* To run tests with coverage in console

```shell
pytest --cov-report term-missing --cov-config=.coveragerc --cov=src src/tests
```

* To run tests with coverage in HTML files

```shell
pytest src/tests --cov=src --cov-config=.coveragerc --cov-report=html:.test-results
```

* To run tests with coverage in XML for Codacy

```shell
pytest src/tests --cov=src --cov-config=.coveragerc --cov-report=xml:coverage-reports/coverage.xml
```
