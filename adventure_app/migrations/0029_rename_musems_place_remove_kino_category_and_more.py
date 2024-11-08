# Generated by Django 5.1.2 on 2024-10-30 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0028_alter_zapis_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Musems',
            new_name='Place',
        ),
        migrations.RemoveField(
            model_name='kino',
            name='category',
        ),
        migrations.RemoveField(
            model_name='parks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.DeleteModel(
            name='Concert',
        ),
        migrations.DeleteModel(
            name='Kino',
        ),
        migrations.DeleteModel(
            name='Parks',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]
