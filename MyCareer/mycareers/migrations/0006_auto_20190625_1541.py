# Generated by Django 2.2.2 on 2019-06-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycareers', '0005_auto_20190625_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_edu_univ',
            name='sub_major',
        ),
        migrations.AddField(
            model_name='tb_edu_univ',
            name='end_type',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tb_edu_univ',
            name='start_type',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
