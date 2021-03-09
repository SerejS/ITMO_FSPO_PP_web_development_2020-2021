# Generated by Django 3.1.7 on 2021-03-06 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.publisher')),
            ],
        ),
    ]
