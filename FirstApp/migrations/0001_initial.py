# Generated by Django 4.2.3 on 2023-08-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prof_pic/')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(max_length=15)),
                ('number', models.TextField(max_length=15)),
                ('age', models.FloatField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=8)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Bodho', 'Bodho'), ('Kristian', 'Kristian')], default='Islam', max_length=10)),
                ('division', models.CharField(max_length=10)),
                ('post_code', models.IntegerField()),
            ],
        ),
    ]
