from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Taty(models.Model):

    objects = None
    TATY_TYPE = [
        ('1', 'Гравюра'),
        ('2', 'Биоорганика'),
        ('3', 'Минимализм'),
        ('4', 'Миниатюра'),
        ('5', 'ЛайнворкНео'),
        ('6', 'ЛайнворкНео'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    taty_type = models.CharField(choices=TATY_TYPE, default='1', max_length=50)



    def __str__(self):
        return '{}, {}, user: {}'.format(self.user, self.name, self.get_taty_type_display(), self.user)


