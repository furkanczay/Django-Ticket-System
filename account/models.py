from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    email = models.EmailField(max_length=200, verbose_name='Eposta Adresi')
    first_name = models.CharField(max_length=150, verbose_name='İsim')
    last_name = models.CharField(max_length=150, verbose_name='Soyisim')
    ticket_admin = models.BooleanField(default=False)
    ticket_agent = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'Üye'
        verbose_name_plural = 'Üyeler'
