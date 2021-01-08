# Generated by Django 2.2.15 on 2021-01-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_remove_about_main_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('market_statement', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_statement', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
