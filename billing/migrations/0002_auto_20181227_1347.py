# Generated by Django 2.1.4 on 2018-12-27 13:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]