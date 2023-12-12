# Generated by Django 4.2.6 on 2023-12-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiseonly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=33),
        ),
    ]
