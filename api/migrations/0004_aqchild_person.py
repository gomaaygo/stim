# Generated by Django 4.1.2 on 2022-11-01 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_person_jaundice'),
    ]

    operations = [
        migrations.AddField(
            model_name='aqchild',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.person'),
        ),
    ]
