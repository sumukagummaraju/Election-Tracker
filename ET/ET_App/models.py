from django.db import models

from ET_App.InterfaceAPI import User


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    state= models.CharField(max_length=40)
    email = models.EmailField()
    password_enc = models.CharField(max_length=100)

class Questions(models.Model):
    questionId = models.IntegerField(primary_key=True)
    question = models.TextField()

class Option(models.Model):
    optionId = models.IntegerField(primary_key=True)
    questionId = models.ForeignKey(Questions,on_delete=models.CASCADE)
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()

class UserSelectedOption(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Questions,on_delete=models.CASCADE)
    optionId = models.ForeignKey(Option,on_delete=models.CASCADE)
    timeRegistered = models.DateTimeField()















