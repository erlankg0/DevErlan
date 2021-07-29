# Generated by Django 3.2.5 on 2021-07-29 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Name Categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименования')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата пуб.')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Дата измен')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изобр')),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'Newses',
                'ordering': ['-title'],
            },
        ),
    ]
