# Generated by Django 4.2.5 on 2023-09-06 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('results', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('age', models.IntegerField()),
                ('country', models.CharField(choices=[('United States of America', 'United States of America'), ('Canada', 'Canada'), ('Mexico', 'Mexico'), ('Europe', 'Europe'), ('Japan', 'Japan'), ('South Korea', 'South Korea')], max_length=24)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifiers.movie')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
