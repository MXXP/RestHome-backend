# Generated by Django 3.0.5 on 2020-05-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_room_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('正在使用', '正在使用'), ('未使用', '未使用')], default='未使用', max_length=10, verbose_name='状态'),
            preserve_default=False,
        ),
    ]
