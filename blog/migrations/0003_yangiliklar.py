# Generated by Django 4.2.3 on 2023-09-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_f_i_sh_royxat_ism_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='rasmlar/images')),
                ('text', models.TextField()),
            ],
        ),
    ]