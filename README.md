# Python Django Web Starter Kit

A modern Django 5.1 starter kit with a sample TODO application. This project has been updated to use the latest Django best practices and security features.

## Features

- **Django 5.1**: Latest stable version with modern features
- **Bootstrap 5**: Modern, responsive UI framework
- **Environment Variables**: Secure configuration using python-decouple
- **Security Best Practices**: Production-ready security settings
- **Modern Python**: Python 3.8+ compatible
- **Static Files Management**: Organized static files structure
- **Clean Architecture**: Following Django best practices

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YuvarajTana/python-django-web-staterKit.git
cd python-django-web-staterKit
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
# On Windows
copy .env.example .env

# On macOS/Linux
cp .env.example .env
```

Edit the `.env` file and set your configuration:

```env
SECRET_KEY=your-unique-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Important**: Generate a secure SECRET_KEY for production. You can use:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to see the application.

## Project Structure

```
python-django-web-staterKit/
├── bookmark/                  # Main application
│   ├── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/            # HTML templates
│   │   └── index.html
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # URL configuration
│   ├── views.py             # View functions
│   └── wsgi.py              # WSGI configuration
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore rules
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Development

### Running Tests

```bash
python manage.py test
```

### Collecting Static Files

For production deployment:

```bash
python manage.py collectstatic
```

### Creating New Apps

```bash
python manage.py startapp <app_name>
```

## Security Notes

- Never commit your `.env` file to version control
- Always use a strong, unique `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Configure `ALLOWED_HOSTS` appropriately for your domain
- Use HTTPS in production (security middleware is pre-configured)

## Production Deployment

When deploying to production:

1. Set `DEBUG=False` in your `.env` file
2. Update `ALLOWED_HOSTS` with your domain names
3. Use a production-grade database (PostgreSQL, MySQL)
4. Configure a proper web server (Gunicorn + Nginx)
5. Set up SSL/TLS certificates
6. Run `collectstatic` to serve static files
7. Use environment variables for all sensitive data

The project includes production-ready security settings that automatically activate when `DEBUG=False`.

## Technologies Used

- **Django 5.1**: Python web framework
- **Bootstrap 5.3**: Frontend framework
- **python-decouple**: Environment variable management
- **SQLite**: Default database (use PostgreSQL/MySQL for production)

## What's New in This Update

This starter kit has been modernized from Django 1.8 (2015) to Django 5.1 (2025):

- ✅ Updated to Django 5.1 with latest best practices
- ✅ Replaced deprecated `MIDDLEWARE_CLASSES` with `MIDDLEWARE`
- ✅ Updated URL patterns from `url()` to `path()`
- ✅ Added environment variable support with python-decouple
- ✅ Implemented modern security settings
- ✅ Updated Bootstrap from 3.3 to 5.3
- ✅ Added comprehensive `.gitignore`
- ✅ Removed hardcoded SECRET_KEY
- ✅ Added static files structure
- ✅ Modernized Python code style
- ✅ Added password validation
- ✅ Improved documentation

## Contributing

Feel free to submit issues and pull requests to improve this starter kit.

## License

This project is open source and available for educational purposes.

## Support

For Django documentation, visit: https://docs.djangoproject.com/

For issues specific to this starter kit, please open an issue on GitHub.
