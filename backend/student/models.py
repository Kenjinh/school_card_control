from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.


class Student(models.Model):
    name = models.CharField(verbose_name=_("Student"), max_length=100)
    email = models.EmailField(verbose_name=_("Email"), unique=True, db_index=True)
    birth_date = models.DateField(verbose_name=_("Birth Date"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school_student'
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
