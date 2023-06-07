# Generated by Django 4.2.1 on 2023-06-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('comment', models.TextField(verbose_name='Комментарии')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('work', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
    ]
