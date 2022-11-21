# Generated by Django 4.1.3 on 2022-11-21 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.director')),
            ],
        ),
    ]
