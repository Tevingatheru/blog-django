# blog-django
This Django-based project aims to create a user-friendly blog website where users can easily access and read blog articles.

### Prerequisites

- Python 3.11.4 or higher
- Django 5.0.3 or higher

# activate environment

`.\blog-env\Scripts\activate`

## Setup:
- Set up a Python virtual environment.
- Install Django: `pip install Django`
- Clone/download the project repository.

## Database:
Run migrations: `python manage.py migrate`

## Run the Development Server:
`python manage.py runserver`

# Super user
To create a superuser, use this command:
`python manage.py createsuperuser`

# Arcitecture

1. [Software Architecture](docs/architecture.md)
2. [Class Diagram](docs/class-diagram.md)
3. [ERD](docs/erd.md)

# Design
Homepage

![Home Page](docs/images/home-page.png)

Details page

![Details Page](docs/images/details-page.png)