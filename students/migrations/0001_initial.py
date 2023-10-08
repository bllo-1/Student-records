# Generated by Django 4.2.2 on 2023-10-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Student Name')),
                ('fname', models.CharField(max_length=500, verbose_name='Father Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('classes', models.CharField(choices=[('5th', 'class 5th'), ('6th', 'class 6th'), ('7th', 'class 7th'), ('8th', 'class 8th'), ('9th', 'class 9th'), ('10th', 'class 10th')], max_length=50)),
                ('marks', models.IntegerField(verbose_name='Percentage')),
                ('enrolled', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]