# SAD

create djnago project : $django-admin startproject docker
create django app : $python3 manage.py startapp dockerd
create image : $sudo docker build -t python-django-app .
run container : $sudo docker run -it -p 8000:8000 python-django-app
