# 🛍️ Catalog Web App (Django)

This is a Django-based educational project for building a product catalog web application. The goal is to gradually implement core backend features using Django and understand best practices in real-world development.


##  What’s Done So Far

- ✅ Project structure set up using Poetry and virtual environment
- ✅ PostgreSQL database connected with `.env` configuration using `python-decouple`
- ✅ Models created for:
  - `Category` (with name and description)
  - `Product` (with name, price, description, FK to category)
- ✅ Admin panel customized:
  - Display columns for both models
  - Filters and search for `Product`
- ✅ Custom management command to load test products
- ✅ Fixtures for loading `Category` and `Product` data
- ✅ Added initial HTML templates (`home.html`, `contacts.html`)
- ✅ Setup static files (Bootstrap + custom CSS)
- ✅ Implemented basic routing and views
- ✅ Protected sensitive data using `.env`

---

### Installation

```bash
git clone https://github.com/bntmzu/SkyPro_Web.git
cd SkyPro_Web
poetry install
```
### Running the Project

```bash
python manage.py runserver
```
