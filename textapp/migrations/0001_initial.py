# Generated by Django 4.0.5 on 2022-06-21 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(blank=True, max_length=100)),
                ('daddress', models.CharField(blank=True, max_length=100)),
                ('dcontact', models.CharField(blank=True, max_length=100)),
                ('demail', models.CharField(blank=True, max_length=100)),
                ('dpassword', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=100)),
                ('uaddress', models.CharField(blank=True, max_length=100)),
                ('ucontact', models.CharField(blank=True, max_length=100)),
                ('uemail', models.CharField(blank=True, max_length=100)),
                ('upassword', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('usertype', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('driverid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='textapp.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('did', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='textapp.driver')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='textapp.user')),
            ],
        ),
    ]
