# LAB - Class 33

## Project: drf-api-permissions-postgres

### Author: Errol Vidad
V.1.0.0 (Pr: https://github.com/Code-Fellows-School-Work/drf-auth/pull/2)

### Links and Resources
- Back-end server url (when applicable): None
- Front-end application (when applicable): None

### Setup
- Install Docker
- Install ThunderClient extension in VS Code

i.e.

- PORT - Port Number: 8000
- DATABASE_URL - None

### How to initialize/run your application (where applicable)

- git clone https://github.com/Code-Fellows-School-Work/drf-auth
- cd drf-auth
- Run the command: docker build -t django_doggos_project .
- Run the command: docker compose up --build
- In the web browser, navigate to http://localhost:8000/api/v1/doggos/

### How to use your library (where applicable)

### Manual Test Procedures:

- While Docker container is up, create superuser
    - run: docker compose run web python manage.py createsuperuser
- Get Token steps:
    - In ThunderClient, create a POST request to http://localhost:8000/api/token/ 
        - Navigate to Body --> JSON and create JSON object using "username": "superuser_username", "password": "superuser_password" 
        - Click send and copy access token
        - Copy refresh token if needed for refresh token steps
- Refresh Token steps:
    - In ThunderClient, create a POST request to http://localhost:8000/api/token/refresh/ 
        - Navigate to Body --> JSON and create JSON object using "refresh": "refresh_token" 
        - Click send and copy access token

- CRUD Routes:
    - [Admin](http://localhost:8000/admin/)
        - Admin panel
    - [Doggo List](http://localhost:8000/api/v1/doggos/)
        - Review list of all doggos
    - [Doggo Detail](http://localhost:8000/api/v1/doggos/<int>)
        - Review detailed info of selected doggo
        - Readonly access for non-owners
        - Edit and delete access for owner
    - [Token Access](http://localhost:8000/api/token/)
        - Provides authenticated users an access and refresh token
    - [Token Refresh](http://localhost:8000/api/token/refresh/)
        - Provides authenticated users a new access token if current access token expired








