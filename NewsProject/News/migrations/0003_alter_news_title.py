# Generated by Django 4.2.2 on 2023-06-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='заголовок'),
        ),
    ]
