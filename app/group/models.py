from django.db import models
from app.teacher.models import Teacher
from app.student.models import Student
from app.other.models import Profession, Room, DayName


class TeamGroup(models.Model):
    title = models.CharField(max_length=221, verbose_name='Guruh Nomi')
    direction = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True, related_name='group_direction', verbose_name='Yonalish')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True,
                                related_name='group_teacher',
                                verbose_name="O'qituvchi")
    students = models.ManyToManyField(Student, verbose_name="Talaba", related_name="group_students")
    image = models.ImageField(upload_to='GroupImages/', null=True, blank=True, verbose_name="Gruh Logotipi")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, verbose_name="Xona",
                             related_name="group_room")
    day = models.ForeignKey(DayName, on_delete=models.CASCADE, null=True, related_name="group_day")
    is_active = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '4. Guruhlar'
        verbose_name_plural = 'Guruhlar'

    def __str__(self):
        return self.title
