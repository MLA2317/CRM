from django.db import models
from app.account.models import Account


class Course(models.Model):
    title = models.CharField(max_length=221, verbose_name='Nomi')
    duration = models.IntegerField(verbose_name='Kurs davomiligi /soati')
    payment = models.FloatField(verbose_name='Tolov')
    lesson_duration = models.IntegerField(verbose_name='Dars davomligi /soati')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kurslar"
        verbose_name_plural = "1. Kurslar"

    def __str__(self):
        return self.title


class Advertising(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Qayerdan kelgan"
        verbose_name_plural = "2.0 Qayerdan kelgan"

    def __str__(self):
        return self.title


class WhereCome(models.Model):
    student = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,  related_name="where_come")
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Qayerdan kelgan"
        verbose_name_plural = "2.1 Qayerdan kelgan"

    def __str__(self):
        return f'{self.student} | {self.advertising}'


class Profession(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Nomi")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Yo'nalishlar"
        verbose_name_plural = "3. Yo'nalishlar"

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=30, verbose_name="Xona")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Xonalar"
        verbose_name_plural = "4. Xonalar"

    def __str__(self):
        return self.title


class DayName(models.Model):
    title = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kunlar"
        verbose_name_plural = "5. Kunlar"

    def __str__(self):
        return self.title
