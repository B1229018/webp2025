# Generated by Django 5.1.6 on 2025-03-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhello', '0002_rename_location_post_coursetitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=150)),
                ('CourseTitle', models.CharField(max_length=150)),
                ('Instructor', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
