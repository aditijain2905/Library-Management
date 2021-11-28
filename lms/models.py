
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


# Create your models here.
class UserInput(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    def __str__(self):
       return self.user.username

class Books(models.Model):
    bookno = models.IntegerField(db_column='BookNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.CharField(db_column='IssueDate', max_length=50, blank=True, null=True)  # Field name made lo       

class Customer(models.Model):
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    bookno = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookNo', blank=True, null=True)  # Field name made lowercase.
    issuedate = models.CharField(db_column='IssueDate', max_length=60, blank=True, null=True)  # Field name made lowercase.


