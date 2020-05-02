# Generated by Django 3.0.5 on 2020-05-02 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_room_old'),
        ('old', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='old',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olds', to='employee.Room'),
        ),
    ]
