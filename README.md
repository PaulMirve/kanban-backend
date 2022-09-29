# Kanban challenge
Backend for the Frontend Mentor's Kanban challenge.

# Frontend
The frontend project for this project can be found [here](https://github.com/PaulMirve/kanban-frontend)

# How to run this project 
**A Postgres database is required to run this project**
- Clone the repository 
- On terminal enter to project folder
- Run command **pip install ./requirements.txt**
- On root folder create a .env file with the next variables
  - DATABASE_NAME
  - DATABASE_PORT
  - DATABASE_PASSWORD
  - DATABASE_HOST
  - DATABASE_USER
  - FRONTEND_ORIGIN
    - The url where the frontend is running
  - ALLOWED_HOST
    - You can leave this variable blank or add the url where the backend server is running
- Run command **python manage.py runserver** 