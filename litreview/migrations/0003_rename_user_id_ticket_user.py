# Generated by Django 4.0.4 on 2022-08-08 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litreview', '0002_rename_user_ticket_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='user',
        ),
    ]