# Trend Blog

Welcome to **Trend Blog**, a blogging platform built using Django. This project allows users to create, read, update, and delete blog posts. It includes an account management system with login, signup, and profile functionalities, along with custom styling for an user experience.

## Features

### Blog Functionality
- **CRUD Operations**: Users can create, read, update, and delete their blog posts.
- **Blog Details**: View detailed pages for individual blogs with dynamic content.

### User Authentication
- **Signup and Login**: Allows users to securely create accounts and log in to access their profile.
- **Error Handling**: Displays messages for invalid credentials.
- **Logout**: Enables users to log out securely.

### Styling and Media
- **Custom Styling**: Includes a design with a CSS file.
- **Media Uploads**: Supports image uploads for profile pictures and blog posts.
- **Static Assets**: Comes with pre-designed banners, icons, and placeholders.

---

## Directory Structure

### Key Components

- **`accounts`**: 
  - Handles user registration, authentication, and profile management.
  - Includes templates for login, signup, and account-related views.
  
- **`blog`**: 
  - Implements core blog features like creating, updating, and displaying blog posts.
  - Stores static assets like CSS, JavaScript, and images for the frontend design.

- **`media`**: 
  - Stores uploaded user images, including profile pictures and blog-related images.

- **`trend_blog`**: 
  - The project’s root configuration containing `settings.py`, `urls.py`, and other configuration files.

### Complete Directory Tree

```plaintext
.
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/accounts
│   │   ├── home.html
│   │   └── signup.html
│   ├── templates/registration
│   │   └── login.html
│   ├── urls.py
│   └── views.py
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── static/blog
│   │   ├── css/styles.css
│   │   ├── images/
│   │   └── js/main.js
│   ├── templates/blog
│   │   ├── blog_detail.html
│   │   ├── create.html
│   │   ├── delete.html
│   │   ├── index.html
│   │   ├── profile.html
│   │   └── update.html
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   ├── blog_images/
│   └── profile_pictures/
└── trend_blog
    ├── settings.py
    ├── urls.py
    └── wsgi.py
