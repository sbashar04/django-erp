# Django ERP

A Dockerized ERP application built with **Django**, **MySQL**, **Docker Compose**, and **Adminer**.
This project includes a custom user authentication system, login page, dashboard, and a modular foundation for building ERP features such as inventory, sales, purchases, accounting, customers, suppliers, and reports.

## Features

* Django-based ERP backend
* Custom user authentication system
* Login page at root domain
* Protected dashboard after login
* MySQL database integration
* Adminer for database management
* Docker and Docker Compose setup
* Modular project structure
* Ready for future ERP modules

## Technology Stack

* Python
* Django
* MySQL
* Docker
* Docker Compose
* Adminer
* HTML
* CSS

## Project Structure

```bash
django-erp/
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   ├── accounts/
│   │   └── login.html
│   └── dashboard/
│       └── index.html
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

Before running this project, make sure you have installed:

* Docker
* Docker Compose
* Git

## Installation

Clone the repository:

```bash
git clone https://github.com/sbashar04/django-erp.git
```

Go to the project directory:

```bash
cd django-erp
```

Build the Docker containers:

```bash
docker compose build
```

Start the containers:

```bash
docker compose up -d
```

## Docker Services

This project uses three main Docker services:

| Service | Description            | Port |
| ------- | ---------------------- | ---- |
| web     | Django application     | 8000 |
| db      | MySQL database         | 3307 |
| adminer | Database management UI | 8081 |

## Environment Variables

The following environment variables are used inside `docker-compose.yml`:

```env
DJANGO_SECRET_KEY=change-this-secret-key
DJANGO_DEBUG=True

DB_NAME=django_erp
DB_USER=erp_user
DB_PASSWORD=erp_password
DB_HOST=db
DB_PORT=3306
```

For production, use a separate `.env` file and do not commit real secrets to GitHub.

## Database Setup

Run migrations:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

Create a superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

## Run the Project

Start all containers:

```bash
docker compose up -d
```

Visit the application:

```text
http://localhost:8000/
```

The root URL will show the login page.

After successful login, the user will be redirected to:

```text
http://localhost:8000/dashboard/
```

## Admin Panel

Django admin panel is available at:

```text
http://localhost:8000/admin/
```

Use the superuser credentials created earlier.

## Adminer Database Access

Adminer is available at:

```text
http://localhost:8080
```

Use the following credentials:

```text
System: MySQL
Server: db
Username: erp_user
Password: erp_password
Database: django_erp
```

## Useful Docker Commands

Start containers:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

Stop containers and remove database volume:

```bash
docker compose down -v
```

View logs:

```bash
docker compose logs -f web
```

Enter Django container shell:

```bash
docker compose exec web bash
```

Run Django shell:

```bash
docker compose exec web python manage.py shell
```

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

## Authentication Flow

The project includes a custom user authentication system.

Current flow:

1. User visits the root URL.
2. Login page is displayed.
3. User enters username and password.
4. After successful login, user is redirected to dashboard.
5. Dashboard is protected and only accessible to authenticated users.
6. Unauthenticated users are redirected back to the login page.

## Planned ERP Modules

The project can be extended with the following ERP modules:

* Company and branch management
* User role and permission management
* Inventory management
* Product category, brand, and unit management
* Supplier management
* Purchase management
* Customer management
* Sales and POS management
* Payment management
* Accounting and ledger system
* Reports and analytics
* HRM and payroll
* Dashboard statistics

## Recommended Development Flow

For a clean ERP development process, build modules in this order:

1. Authentication and user roles
2. Company and branch setup
3. Product, category, brand, and unit
4. Supplier management
5. Purchase management
6. Customer management
7. Sales and invoice management
8. Payment and due management
9. Accounting ledger
10. Reports and dashboard analytics

## Git Ignore

Make sure sensitive files are not committed:

```bash
.env
.env.*
db.sqlite3
media/
staticfiles/
__pycache__/
venv/
```

You may keep an `.env.example` file in the repository to show required environment variables.

## License

This project is open-source and available for learning and development purposes.

## Author

Developed by **Md Shafiul Bashar**.
