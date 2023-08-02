from django.db import models
from app.account.models import Account
from app.other.models import Profession


class Teacher(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,
                                limit_choices_to={'is_teacher': True, 'is_active': True})
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Ustozlar"
        verbose_name_plural = "Ustozlar"

    def __str__(self):
        return f'{self.teacher} {self.profession} teacher'
