# Generated by Django 4.1.3 on 2023-08-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Last name')),
                ('phone', models.CharField(db_index=True, max_length=16, null=True, unique=True, verbose_name='Phone number')),
                ('birth_year', models.IntegerField(blank=True, null=True, verbose_name='Birth year')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='accounts/', verbose_name='User avatar')),
                ('role', models.IntegerField(choices=[(0, 'Staff'), (1, 'Teacher'), (2, 'Student'), (3, 'demo')], default=1)),
                ('gender', models.IntegerField(choices=[(0, 'None'), (1, 'Male'), (2, 'Female')], default=0)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super user')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff user')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Teacher')),
                ('is_student', models.BooleanField(default=False, verbose_name='Student')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active user')),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='Date login')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]