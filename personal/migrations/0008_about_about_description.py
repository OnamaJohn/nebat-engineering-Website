# Generated by Django 2.2.15 on 2021-01-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_description',
            field=models.TextField(default='Nebat Engineering Experts Ltd was founded by an electrical and telecommunications engineer,Ivan Muyomba in 2017 and has since grown progressively into a leading company in the business of power line works and the related engineering works.Development,revitalization and maintenance of low,medium and high voltage power transmission lines is the most recognized strategic business divisions of Nebat Engineering Experts Ltd in addition to building construction works,network communication channels,generator works,solar installations,car tracking systems and so many others embedded in the general sales.'),
            preserve_default=False,
        ),
    ]
