# Generated by Django 4.1.3 on 2023-08-02 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kurslar', 'verbose_name_plural': '1.Kurslar'},
        ),
        migrations.AlterModelOptions(
            name='dayname',
            options={'verbose_name': 'Kunlar', 'verbose_name_plural': '5.Kunlar'},
        ),
        migrations.AlterModelOptions(
            name='profession',
            options={'verbose_name': "Yo'nalishlar", 'verbose_name_plural': "3.Yo'nalishlar"},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Xonalar', 'verbose_name_plural': '4.Xonalar'},
        ),
    ]
