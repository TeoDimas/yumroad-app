# Yumroad

Yumroad is a robust scaffold designed to accelerate the development of modern Flask applications. Tailored for creators, developers, and hackathon participants, it abstracts away common boilerplate — including user registration, OAuth integration, team management, and billing — allowing you to focus on building your unique ideas and prototypes rapidly.

Whether you're launching a digital product marketplace or iterating on your next SaaS solution, Yumroad offers a production-ready foundation you can trust.

---

## 🚀 Key Features

- **User Authentication:** Secure login, registration, and OAuth integration out-of-the-box.  
- **Stripe Checkout:** Seamlessly handle one-time product purchases with integrated credit card payments and receipt generation.  
- **Email Notifications:** Automated email delivery to keep users informed and engaged.  
- **Admin Dashboard:** Intuitive interface for managing application data and user activities.

---

## 🧱 Technology Stack

Yumroad leverages a carefully curated selection of technologies to ensure performance, maintainability, and developer productivity:

- **Web Framework:** [Flask](https://flask.palletsprojects.com/) – Lightweight and flexible Python web framework.  
- **Database & ORM:** SQLAlchemy and Flask-SQLAlchemy for powerful database interaction and migrations.  
- **Forms & Validation:** Flask-WTF and WTForms with email validation.  
- **Authentication:** Flask-Login for session management.  
- **Task Queue:** Redis-backed job queues via Flask-RQ2 and RQ Dashboard.  
- **Payments:** Stripe API integration for secure payment processing.  
- **Caching:** Flask-Caching to improve performance and scalability.  
- **Asset Management:** Flask-Assets with CSS and JS minification.  
- **Email Service:** Flask-Mail for email handling and notifications.  
- **Error Monitoring:** Sentry SDK for real-time error tracking.

### Development Tools

- Testing: pytest, pytest-flask, pytest-cov  
- Debugging: Flask-DebugToolbar  
- Code Quality: flake8  
- Mocking & Testing Helpers: vcrpy, fakeredis  

---

## 🎯 Use Cases

- **Hackathons:** Jumpstart your MVP without reinventing essential functionality.  
- **Digital Creator Platforms:** Effortlessly sell music, software, or digital content directly to your audience.  
- **SaaS Applications:** Establish a scalable Flask-based SaaS foundation with user management and payment processing included.

---

## 📦 Installation

### Prerequisites

- Python 3.x (download from [python.org](https://www.python.org/))  
- Optional but recommended: virtual environment setup

### Setup Steps

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
  ```
---

## 📦 Running the Application

After installing dependencies and activating your virtual environment, start the application using one of the following commands:

```bash
./manage.py server
# OR
FLASK_APP=manage FLASK_ENV=development flask run
  ```
---

## 🛠️ Development Workflow

To set up your development environment and seed the database with initial data, run the following commands:

```bash
source env/bin/activate    # Activate your virtual environment
./manage.py resetdb        # Reset and seed the database
FLASK_APP=manage FLASK_ENV=development flask run  # Start the development server
  ```

## ⚙️ Configuration

Set up your environment variables by exporting them in your shell or by placing them in a `.env` file. The key variables include:

```bash
export STRIPE_WEBHOOK_KEY='your_webhook_key'
export STRIPE_PUBLISHABLE_KEY='your_publishable_key'
export STRIPE_SECRET_KEY='your_secret_key'
export MAIL_USERNAME='your_email_username'
export MAIL_PASSWORD='your_email_password'
export FLASK_ENV=development
export FLASK_APP="yumroad:create_app"
  ```
---

## 🧪 Running Tests

To run the full test suite locally with coverage reporting, use the following commands:

```bash
APPNAME_ENV=test ./manage.py test --coverage
# Or, run tests using pytest directly:
pytest --cov=yumroad --cov-report=term-missing

