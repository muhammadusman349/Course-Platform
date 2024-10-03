# 📚 Django Course Platform

A robust **Django-powered** online learning platform designed for seamless course management, user enrollments, and a dynamic interface.

## 🚀 Features
- 🔐 **User Authentication**: Secure sign-up and login functionality.
- 📖 **Course Management**: Admins can create, update, and manage courses.
- 👥 **Enrollments**: Track each Course progress.
- ✉️ **Email Notifications**: Automated notifications to keep students informed.
- 🎨 **Responsive Design**: Built with Tailwind CSS for modern, responsive UI.

## 🛠️ Installation

### Prerequisites:
- Python 3.x
- Django
- Node.js (for Tailwind CSS setup)
- npm (for managing front-end dependencies)

### Setup:

```bash
# Clone the repository
git clone https://github.com/muhammadusman349/Course-Platform.git

# Navigate into the project directory
cd Course-Platform

# Install required dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver

```


## 🌐 Tailwind CSS Setup

Ensure that Node.js and npm are installed, then run the following commands to set up Tailwind CSS:

```bash
# Install Tailwind
python manage.py tailwind install

# Compile Tailwind CSS
python manage.py tailwind build

```
## 🖥️ Technologies
- **Backend**: Django, Python
- **Frontend**: Tailwind CSS, HTML, JavaScript
- **Database**: SQLite (default, can be changed)
- **Other Tools**: Node.js, npm (for managing front-end assets)

## 📜 License
This project is licensed under the MIT License.
