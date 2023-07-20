# baseUsers

A template project with user authentication

Backend: FastAPI + SQLAlchemy + PostgreSQL

Frontend: ReactJS

Features:

There is a running website: https://zinchenkomig.com/

Not much interesting functionality for users right now. Users can just sign up and login.
There is a superuser role with an admin panel, where admins can manage users' information.

But inside I have a CI/CD set up and running. Pytest tests are run on every pull request. Then a container is built and deployed on my VPS.
Right now I am on to building a strong architecture for a comfortable development process.

I use HTTP Only JWT token to manage users sessions.


More features are comming...
