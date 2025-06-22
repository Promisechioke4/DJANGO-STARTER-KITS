# 🚀 Django REST API Starter Kit

Kickstart your next API project with Django + DRF + JWT Auth + Swagger UI.

## ✅ Features
- Custom User Model (Email Login)
- User Registration & Login with JWT
- Token Refresh
- DRF + PostgreSQL (or SQLite)
- Swagger UI for API testing
- Modular Project Layout
- Custom Permissions (`IsOwner`, `IsAdminUser`)

## 🛠 Setup
```bash
git clone https://github.com/yourname/django-starter-kit.git
cd django-starter-kit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 👤 Custom User Model
This project uses a custom user model (`CustomUser`) with email as the login field.
To change user authentication logic, edit `users/models.py` and `AUTH_USER_MODEL` in `settings.py`.

## 🔐 Custom Permissions

### `IsOwner`
Grants access only if the authenticated user owns the object.

### `IsAdminUser`
Allows access only to admin users (`is_staff=True`).

To use these in views:
```python
from users.permissions import IsOwner, IsAdminUser
```

## 🔐 Authentication Endpoints
- `POST /api/register/` – User registration
- `POST /api/token/` – Obtain JWT token
- `POST /api/token/refresh/` – Refresh token

## 📁 Project Structure
```text
django_starter_kit/
├── core/              # Project settings and URLs
├── users/             # User app (models, views, permissions, serializers)
├── requirements.txt   # Dependencies
├── .env.example       # Environment variable template
├── README.md          # Project documentation
└── LICENSE            # MIT License
```


## 📜 License
MIT License - Free to use for personal & commercial projects.