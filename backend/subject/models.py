from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.

class Subject(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    hourly_load = models.IntegerField(verbose_name=_("Hourly Load"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school_subject'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
