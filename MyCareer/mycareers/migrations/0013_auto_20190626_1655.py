# Generated by Django 2.2.2 on 2019-06-26 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycareers', '0012_auto_20190626_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_project',
            old_name='start',
            new_name='project_start',
        ),
        migrations.RenameField(
            model_name='tb_reward',
            old_name='start',
            new_name='reward_start',
        ),
    ]
