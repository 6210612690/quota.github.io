# Generated by Django 3.2.7 on 2021-09-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('registered_course', models.ManyToManyField(blank=True, related_name='students', to='courses.Course')),
            ],
        ),
    ]
