# Generated by Django 3.2.7 on 2021-10-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_publishing_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=50)),
                ('nip', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
