# Generated by Django 2.0 on 2017-12-28 23:45

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), blank=True, size=None)),
                ('role', models.PositiveSmallIntegerField(default=0, verbose_name=[(0, 'Thing'), (1, 'Agent'), (2, 'Place'), (3, 'Event')])),
                ('identifiers', models.TextField()),
                ('description', models.TextField()),
                ('source', models.TextField(blank=True, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Instance',
                'verbose_name_plural': 'Instances',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), blank=True, size=None)),
                ('name', models.TextField()),
                ('definition', models.TextField(blank=True, null=True)),
                ('is_category', models.BooleanField(default=False)),
                ('source', models.TextField(blank=True, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('parents', models.ManyToManyField(blank=True, related_name='parent_types', to='meta.Type')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Type'),
        ),
    ]