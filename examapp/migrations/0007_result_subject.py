# Generated by Django 4.2.5 on 2023-09-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0006_customuser_subject_alter_quesmodel_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
