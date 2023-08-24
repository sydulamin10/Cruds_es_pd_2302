# Generated by Django 4.2.3 on 2023-08-08 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_custom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.profile'),
        ),
        migrations.CreateModel(
            name='Custom_User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.profile')),
            ],
        ),
    ]