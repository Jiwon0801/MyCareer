# Generated by Django 2.2.2 on 2019-06-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycareers', '0004_auto_20190625_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_edu_univ',
            name='day_yn',
            field=models.TextField(blank=True, null=True),
        ),
    ]
