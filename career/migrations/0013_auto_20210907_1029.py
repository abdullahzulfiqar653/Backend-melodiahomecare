# Generated by Django 3.2.7 on 2021-09-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0012_auto_20210907_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_forms',
            name='application_date',
            field=models.DateField(verbose_name='Date of Application'),
        ),
        migrations.AlterField(
            model_name='apply_forms',
            name='available',
            field=models.DateField(verbose_name='On what date could you be avilable for work?'),
        ),
    ]
