# Generated by Django 2.1.3 on 2018-11-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20181101_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
