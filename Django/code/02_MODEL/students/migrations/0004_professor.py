# Generated by Django 4.2.5 on 2023-09-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_gpa_stduent_cgpa_remove_stduent_is_graduated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=100)),
                ('room', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
