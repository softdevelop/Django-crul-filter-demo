from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(models.Model):
    CONST_MALE = 0
    CONST_FEMALE = 10

    CONST_SEX = (
        (CONST_MALE, _('male')),
        (CONST_FEMALE, _('female')),
    )
    name = models.CharField(max_length=200)
    sex = models.PositiveSmallIntegerField(choices=CONST_SEX, default=CONST_MALE)
    age = models.PositiveSmallIntegerField()