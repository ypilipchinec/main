# Generated by Django 3.2.9 on 2021-12-17 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='camers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('address', models.GenericIPAddressField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('guid', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='dvn_camers',
        ),
        migrations.DeleteModel(
            name='grz_camers',
        ),
        migrations.DeleteModel(
            name='pes_camers',
        ),
        migrations.DeleteModel(
            name='pvn_camers',
        ),
    ]
