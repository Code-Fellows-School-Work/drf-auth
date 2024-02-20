# LAB - Class 32

## Project: drf-api-permissions-postgres

### Author: Errol Vidad
V.1.0.0 (Pr: https://github.com/Code-Fellows-School-Work/drf-api-permissions-postgres/pull/1)

### Links and Resources
- Back-end server url (when applicable): None
- Front-end application (when applicable): None

### Setup
- Install Docker

i.e.

- PORT - Port Number: 8000
- DATABASE_URL - postgres://USER:PASSWORD@db:5432/DBNAME

### How to initialize/run your application (where applicable)

- git clone https://github.com/Code-Fellows-School-Work/drf-api-permissions-postgres.git
- cd drf-api-permissions-postgres
- Run the command: docker build -t django_doggos_project .
- Run the command: docker compose up --build
- In the web browser, navigate to http://localhost:8000/api/v1/doggos/

### How to use your library (where applicable)
### Tests
How do you run tests?

- docker exec -it <container_name_or_id> python manage.py test




