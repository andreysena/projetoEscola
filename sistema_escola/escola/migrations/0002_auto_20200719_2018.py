# Generated by Django 3.0.8 on 2020-07-19 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='FK_Serie',
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
    ]