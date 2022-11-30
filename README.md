# FastAPI Basic
FastAPI의 기능을 자세히 알아보기 위해 작성된 프로젝트입니다.    
아이템 개발보다는 기능 구현에 초점에 맞춰 개발되었습니다.

약 2,000개의 더미 데이터를 postgreSQL에 적재하여,
CURD 기능을 비동기식으로 수행할 수 있도록 구현하였습니다.   
(더미 데이터는 고객 정보와 특정 고객의 카드 정보입니다.)


## Installation
```python
pip install -r .\requirement.txt
```


## Run
```python
python3 main.py
```

## Skill Stack
* PostgreSQL
* SQLAlchemy
* FastAPI
* Python
* Redis


## Features
* SQLAlchemy Async Session
* Dependencies for specific permission
* authentication
* Cache


## Naming Convention
* `Python` - https://peps.python.org/pep-0008/
* `SQLAlchemy` - https://docs.sqlalchemy.org/en/14/core/constraints.html
