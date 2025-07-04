from django.db import models
from django.contrib.auth.hashers import make_password

class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        # Hash the password only if it is not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
        ordering = ['username']
