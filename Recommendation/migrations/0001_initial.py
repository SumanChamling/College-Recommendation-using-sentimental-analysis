# Generated by Django 3.2.13 on 2022-04-26 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Recommendation_faculty',
            },
        ),
        migrations.CreateModel(
            name='oldSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastSchool', models.CharField(max_length=200)),
                ('student_email', models.EmailField(default=True, max_length=254)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=200)),
                ('registered_email', models.EmailField(default=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=500)),
                ('collegeName', models.CharField(max_length=200)),
                ('collegeLocation', models.CharField(max_length=200)),
                ('collegeReview', models.CharField(max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=True, null=True)),
                ('data', models.IntegerField(blank=True, default=True, null=True)),
                ('facultyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommendation.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=80)),
                ('phone', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddColleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('phone', models.IntegerField()),
                ('description', models.CharField(max_length=499, null=True)),
                ('website', models.URLField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('facultyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommendation.faculty')),
            ],
        ),
    ]
