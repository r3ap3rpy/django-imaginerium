# Generated by Django 4.1.6 on 2023-02-08 08:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]