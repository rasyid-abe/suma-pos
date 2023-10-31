# Generated by Django 3.2.13 on 2023-10-28 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=255)),
                ('expired', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_apps.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_apps.user')),
            ],
        ),
    ]