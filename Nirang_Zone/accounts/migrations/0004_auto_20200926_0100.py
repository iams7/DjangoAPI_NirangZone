# Generated by Django 3.1.1 on 2020-09-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200926_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.EmailField(default='admin@gmail.com', max_length=100),
        ),
    ]