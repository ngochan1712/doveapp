# Generated by Django 4.2 on 2023-05-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0005_my_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_goal',
            name='date1',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='personalin_fo',
            name='gioitinh',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='personalin_fo',
            name='place',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
