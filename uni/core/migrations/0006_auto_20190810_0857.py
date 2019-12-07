# Generated by Django 2.2.4 on 2019-08-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_course_date_of_starting'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(blank=True, help_text='Дата подвешивания курса', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='information',
            field=models.TextField(blank=True, help_text='Краткая информация о курсе', max_length=1000, null=True),
        ),
    ]
