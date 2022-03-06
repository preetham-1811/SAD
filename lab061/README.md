1. Create django project: $sudo docker-compose run web django-admin startproject counter </br>
2. Create django app: $sudo docker-compose run web python3 manage.py startapp counterapp </br>
3. Run container: $sudo docker-compose up </br>
4. Execute: $sudo docker exec -it counter_web_1 bash
5. Make Migrations & migrate: $python3 manage.py makemigrations counterapp and $python3 manage.py migrate 