# Generated by Django 2.2.2 on 2019-06-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycareers', '0014_auto_20190626_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_basic',
            old_name='army_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_career',
            old_name='career_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_cert',
            old_name='cert_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_edu_high',
            old_name='high_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_edu_univ',
            old_name='uni_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_education',
            old_name='edu_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='tb_user_filter',
            old_name='filter_start',
            new_name='start',
        ),
    ]
