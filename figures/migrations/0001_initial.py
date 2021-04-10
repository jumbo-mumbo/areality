# Generated by Django 3.1.5 on 2021-04-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('photo', models.ImageField(upload_to='figures/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]