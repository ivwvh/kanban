# Generated by Django 4.2.1 on 2023-06-02 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название канбана')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kanbans', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Канбан',
                'verbose_name_plural': 'Канбаны',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, verbose_name='Описание задачи')),
                ('status', models.CharField(default='PLANNED', max_length=100, verbose_name='Статус')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('creation_time', models.TimeField(auto_now_add=True)),
                ('assigned_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('assigned_time', models.TimeField(blank=True, default=django.utils.timezone.now)),
                ('deadline_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('deadline_time', models.TimeField(blank=True, default=django.utils.timezone.now)),
                ('completed_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('completed_time', models.TimeField(blank=True, default=django.utils.timezone.now)),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_owner', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('kanban', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='kanban_tasks', to='kanbanka.kanban', verbose_name='Канбан')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]