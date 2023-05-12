# Generated by Django 4.2.1 on 2023-05-12 06:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('titleru', models.CharField(blank=True, max_length=200, null=True)),
                ('titleeng', models.CharField(blank=True, max_length=200, null=True)),
                ('titleeturk', models.CharField(blank=True, max_length=200, null=True)),
                ('rasm1', models.FileField(upload_to='')),
                ('rasm2', models.FileField(upload_to='')),
                ('rasm3', models.FileField(upload_to='')),
                ('text1', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1ru', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1eng', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1turk', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomru', models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomeng', models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomturk', models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomru', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomeng', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomturk', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('isSubmyu', models.BooleanField(default=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('url', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomru', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomeng', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('nomturk', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1ru', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1eng', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text1turk', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text2', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text2ru', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text2eng', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('text2turk', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('rasm1', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm2', models.FileField(blank=True, null=True, upload_to='')),
                ('url', models.CharField(blank=True, max_length=40, null=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to='')),
                ('menyu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menyu')),
            ],
        ),
    ]
