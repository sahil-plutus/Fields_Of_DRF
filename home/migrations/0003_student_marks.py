# Generated by Django 4.0.3 on 2022-03-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
