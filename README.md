# BOOOK CRUD APP
Follow these steps to set up and run the project on your local machine.
1. Create Virtual Environment:
```python -m venv my-env```
2. Activate the virtual environment:
For Windows: ```.\my-env\Scripts\activate.bat```
In macOs and Linux: ```source./my-env/bin/activate```
3. Now, my-env will be activated and Inside it install Django.
```pip install django```
4. Install two more dependencies for APIs.
```pip install djangorestframework django-cors-headers```
5. Install Pillow for image handling:
```python -m pip install Pillow```
6. Run the development server:
```python manage.py runserver```
Visit http://localhost:8000/api/books/ in your web browser to access the API for books.




