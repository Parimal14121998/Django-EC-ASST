from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
              
