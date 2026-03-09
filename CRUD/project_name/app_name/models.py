from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    role = models.CharField(max_length=100)

    # python manage.py migrate           | models create pannitu intha 3 uh commands run pannanum
    # python manage.py makemigrations
    # python manage.py migrate

    # python manage.py createsuperuser    | admin panel ku user create pannanum na intha command run pannanum

    
