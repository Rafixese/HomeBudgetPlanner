# Generated by Django 4.1 on 2023-02-11 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetobj',
            options={'permissions': [('can_view_budgetobj', 'Can view budget objects'), ('can_manage_budgetobj', 'Can manage budget objects')]},
        ),
    ]
