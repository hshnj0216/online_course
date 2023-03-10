# Generated by Django 3.1.3 on 2023-02-20 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20230220_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]
