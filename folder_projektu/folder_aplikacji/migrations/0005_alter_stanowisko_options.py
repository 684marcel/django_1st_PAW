# Generated by Django 5.1.3 on 2024-12-03 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0004_alter_osoba_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stanowisko',
            options={'verbose_name': 'Stanowisko', 'verbose_name_plural': 'Stanowiska'},
        ),
    ]