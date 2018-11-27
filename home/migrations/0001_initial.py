# Generated by Django 2.1.2 on 2018-11-24 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', height_field='url_height', upload_to='images/', width_field='url_width')),
                ('source', models.CharField(max_length=200, null=True)),
                ('belong', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('describe', models.CharField(max_length=200, null=True)),
                ('text', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('public', models.CharField(max_length=20, null=True)),
                ('display', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('source', models.CharField(max_length=200)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Image')),
            ],
        ),
    ]
