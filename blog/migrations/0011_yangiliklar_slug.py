# Generated by Django 4.2.3 on 2024-02-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_avtive_comment_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='slug',
            field=models.SlugField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]