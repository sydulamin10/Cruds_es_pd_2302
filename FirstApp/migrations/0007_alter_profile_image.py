# Generated by Django 4.2.3 on 2023-08-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0006_remove_custom_user1_prof_delete_custom_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='def.png', null=True, upload_to='prof_pic/'),
        ),
    ]