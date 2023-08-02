from django.db import models
from app.account.models import Account
from app.other.models import Profession


class Student(models.Model):
    student = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,
                                limit_choices_to={'is_student': True, 'is_active': True})
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)
    payment = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "O'quvchilar"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return f'{self.student} | {self.payment}'
