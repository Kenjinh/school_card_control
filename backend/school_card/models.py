import json
from django.db import models
from django.utils.translation import ugettext as _

from student.models import Student
from subject.models import Subject


# Create your models here.

class SchoolCard(models.Model):
    delivery_date = models.DateField(verbose_name=_('Delivery Date'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("Student"))

    def __str__(self):
        return self.student

    class Meta:
        db_table = 'school_school_card'
        verbose_name = _('School Card')
        verbose_name_plural = _('School Cards')


class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Subject"))
    school_card = models.ForeignKey(SchoolCard, on_delete=models.CASCADE, verbose_name=_("School Card"))
    grade = models.DecimalField(verbose_name=_("Grade"), max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'school_school_card_grade'
        verbose_name = _('School Card Grade')
        verbose_name_plural = _('School CardGrades')
