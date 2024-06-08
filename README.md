# CarSearch - Django REST API (DRF)
CarSearch is a Django REST API project that I have created while learning the DRF. It provides functionalities to manage and search car listings. This project includes features like CRUD operations for car listings, advanced search capabilities, and user authentication.

## Features Implemented
- **Authentication**: *JWT*, *Token Authentication*, *Basic Authentication*
- **Permissions**: *Custom Permissions*
- **Throttling**: *Custom Throttle*, *ScopedRated Throttle*
- **Pagination**: *PageNumber Pagination*
- **Routers**: *BasicRouter*
- **Serializers**: *ModelSrializer*
- **Validators**: *Custom Validators*
- **Generic Views**
- **Status Codes**

## Libraries Used
- **Django**
- **Django Rest Framework**
- **Django Rest Framework - SimpleJwt**

## File Structure
- **carSearch/**: Core Django project directory.
- **carSearch_app/**: Django app for car search functionality.
- **user_app/**: Django app for user authentication.


## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/omdusane/carSearch-django-rest.git
2. Navigate to the project directory:
   ```sh
   cd carSearch-django-rest
3. Create and activate a virtual environment and intall the dependencies:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
4. Run Migrations:
   ```sh
   python manage.py migrate
5. Start the development server:
   ```sh
   python manage.py runserver
6. Open your browser and navigate to `http://localhost:8000`.