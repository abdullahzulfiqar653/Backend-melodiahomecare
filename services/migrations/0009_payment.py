# Generated by Django 3.2.6 on 2021-09-01 09:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20210831_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500, verbose_name='Heading')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Payment/')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
