from django.db import models

# Create your models here.
# mvt = model view template 
# django uses sqlite databse by default and connection is already made in settings.py file

# models  
# models are responsible for maintaining data in database 

class Employee(models.Model): #Employee is the table name that will be created in database
    eno = models.IntegerField()
    ename = models.CharField(max_length =20 )
    esal = models.FloatField()
    eadd = models.CharField(max_length =64 ) 
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now=True) 
# autonow it will take current time

    def __str__(self):
        return self.email



# The above will not create the table in database so for that we need to create migrations
# python manage.py makemigrations(makemigration will create the migration file of models.py and it 
# will convert into sql and at app level it will inside migration it will create initial.py file inside
# that model will be created )

# In initial.py inside model seprate id will be created by default that will be unique.
# any changes in models.py after makemigration it will not reflect .
# after migration now we need to run the initial.py file so we need to use migrate
# python manage.py migrate 
# it will make tables for all the apps (installed app in settings.py file i.e for predefined apps)

#to see table is created in database or not we need to use admin site i.e we need to create superuser
#python manage.py createsuperuser
# un:admin
#pss:Saloni123

# we need to register the model in admin.py file