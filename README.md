# Trend Blog

Welcome to **Trend Blog**, a robust blogging platform built using Django 5.1.4. This project allows users to create, read, update, and delete blog posts with custom user authentication, profile management, and production-ready security features.

## Features

### Blog Functionality
- **CRUD Operations**: Users can create, read, update, and delete their blog posts
- **Soft Delete**: Blog posts are soft-deleted for recovery options
- **Categories**: Organize blogs by Food, Tech, Life, and News categories
- **SEO-Friendly URLs**: Auto-generated slugs for better discoverability
- **Permission Controls**: Users can only edit/delete their own posts

### User Authentication
- **Custom User Model**: Extended user profiles with bio, quote, and profile pictures
- **Signup and Login**: Secure account creation and authentication
- **Protected Routes**: Login-required views for creating and managing content
- **Error Handling**: User-friendly messages for all operations

### Security Features
- **Environment-Based Configuration**: Secrets managed via `.env` file
- **CSRF Protection**: Built-in protection against cross-site request forgery
- **Session Security**: HTTPOnly cookies and configurable session age
- **Logging**: Comprehensive logging for debugging and audit trails
- **Production-Ready**: Security headers and HTTPS enforcement for production

### Media & Assets
- **Image Uploads**: Support for blog images and profile pictures
- **Static File Management**: Efficient static file serving with WhiteNoise
- **Responsive Design**: Custom CSS styling for optimal user experience

---

## Setup and Running the Project

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/lspaudel/trend_blog
cd trend_blog
```

### 2. Create Virtual Environment

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

**Create `.env` file in project root:**
```bash
cp .env.example .env
```

**Edit `.env` and configure:**
```env
SECRET_KEY=your-unique-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Generate a secure SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> ⚠️ **IMPORTANT**: Never commit the `.env` file to version control! It contains sensitive information.

### 5. Database Setup

**For fresh installation:**
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

**For existing database:**
> **Note**: This project now uses a CustomUser model. If you have an existing database, you may need to reset it or perform complex migrations.

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```
You'll be prompted for username, email, and password.

### 7. Run Development Server

```bash
python manage.py runserver
```

- **Homepage**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Signup**: `http://127.0.0.1:8000/accounts/signup/`
- **Login**: `http://127.0.0.1:8000/accounts/login/`

---

## Testing

### Run Tests

```bash
# Using Django test runner
python manage.py test

# Using pytest (recommended)
pytest

# With coverage report
pytest --cov=blog --cov=accounts --cov-report=html
```

### Check for Issues

```bash
# Check for configuration issues
python manage.py check

# Check deployment readiness
python manage.py check --deploy
```

---

## Project Structure

```plaintext
.
├── accounts/              # User authentication and profiles
│   ├── models.py         # CustomUser model
│   ├── forms.py          # SignUpForm
│   ├── views.py          # Signup, login views
│   └── templates/
├── blog/                  # Core blogging functionality
│   ├── models.py         # Blog model with soft delete
│   ├── forms.py          # BlogForm
│   ├── views.py          # CRUD operations
│   ├── static/blog/      # CSS, JS, images
│   └── templates/
├── trend_blog/           # Project configuration
│   ├── settings.py       # Environment-based settings
│   └── urls.py           # URL routing
├── media/                # User uploads
├── staticfiles/          # Collected static files
├── .env.example          # Environment template
├── .gitignore           # Git ignore patterns
├── requirements.txt      # Python dependencies
├── pytest.ini           # Test configuration
└── manage.py            # Django management script
```

---

## Key Improvements

This project has been enhanced with:

**Security Hardening**
- Environment-based configuration (no hardcoded secrets)
- AUTH_USER_MODEL properly configured
- Security middleware and headers
- Production-ready settings

**Better Error Handling**
- User-friendly error messages
- Comprehensive logging
- Permission checks on all operations

**Code Quality**
- Soft delete for data recovery
- Custom model managers
- Admin interface enhancements
- SEO-friendly slugs

**Testing Infrastructure**
- Pytest configuration
- Coverage reporting setup

---

## Production Deployment

Before deploying to production:

1. **Set `DEBUG=False`** in `.env`
2. **Configure proper `ALLOWED_HOSTS`**
3. **Use PostgreSQL or MySQL** instead of SQLite
4. **Set up HTTPS** with SSL certificate
5. **Run `collectstatic`**: `python manage.py collectstatic`
6. **Configure proper logging** and error tracking
7. **Set up regular backups**

For detailed deployment instructions, see the setup guide in the project artifacts.

---

---

## Support

For issues, questions, or contributions, please open an issue on GitHub.
