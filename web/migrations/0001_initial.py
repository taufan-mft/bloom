# Generated by Django 3.1.1 on 2020-09-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kota', models.TextField()),
                ('status', models.TextField(choices=[('Tersedia', 'Tersedia'), ('Penuh', 'Penuh')], default='Tersedia')),
            ],
        ),
    ]