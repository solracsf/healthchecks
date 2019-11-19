# Generated by Django 2.2.6 on 2019-11-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_profile_deletion_notice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_active_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sms_limit',
            field=models.IntegerField(default=5),
        ),
    ]
