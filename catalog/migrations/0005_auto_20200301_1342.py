# Generated by Django 3.0.3 on 2020-03-01 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200301_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_edit_athor', 'Edit a specific author.'), ('can_add_author', 'Add a new author.'), ('can_delete_author', 'Delete a specific author'))},
        ),
    ]
