# Generated by Django 4.1.2 on 2022-11-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_aqchild_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqchild',
            name='result',
            field=models.IntegerField(blank=True, null=True, verbose_name='Resultado'),
        ),
    ]