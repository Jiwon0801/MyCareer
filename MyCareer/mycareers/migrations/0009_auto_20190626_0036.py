# Generated by Django 2.2.2 on 2019-06-26 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycareers', '0008_auto_20190625_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_career',
            name='career_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tb_career',
            name='career_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tb_cert',
            name='cert_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tb_cert',
            name='cert_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
