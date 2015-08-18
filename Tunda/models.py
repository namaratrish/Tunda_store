from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRegistration(models.Model):
    user = models.OneToOneField(User)
    City = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)

    class Meta:
        db_table = "Users"

    def __unicode__(self):

        return self.user.username



