# Generated by Django 3.2.8 on 2021-10-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taty',
            name='taty_type',
            field=models.CharField(choices=[('1', 'Гравюра'), ('2', 'Биоорганика'), ('3', 'Минимализм'), ('4', 'Миниатюра'), ('5', 'ЛайнворкНео'), ('6', 'ЛайнворкНео')], default='1', max_length=50),
        ),
    ]
