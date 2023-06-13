===== COVID HOSPITAL SERVICE AVALIABILY APP ===== 
step 1 => python -m venv myenv 
step 2 => myenv\Scripts\activate //Linux or Mac => source myenv/bin/activate 
step 3 => pip install django 
Upgrade pip => python.exe -m pip install --upgrade pip 
check Django version => django-admin --version 
step 4 => django-admin startproject covidhospitalapp 
step 5 => cd covidhospitalapp 
step 6 => django-admin startapp covidapp
step 7 => python manage.py makemigrations
step 8 => python manage.py migrate
step 9 => python manage.py createsuperuser

step 10 => python manage.py runserver or python manage.py runserver 8080 


pip freeze > requirements.txt 
pip install -r requirements.txt 
deactivate //deactivae vertualenvrinment# covidhospitalapp-django

====== Project Details ============================
1-Admin Table showing format change
2-custom template for html (custom function)
3-use filter to database for getting data
4-use class base view to show details page
