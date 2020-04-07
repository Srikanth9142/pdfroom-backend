# Generated by Django 3.0.2 on 2020-04-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('fileUrl', models.CharField(max_length=150)),
                ('coverphoto', models.ImageField(upload_to='media/')),
                ('author', models.CharField(max_length=150, null=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('photoid', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Analytic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.Book')),
            ],
        ),
    ]
