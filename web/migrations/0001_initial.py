# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moderator', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('contact_group', models.ForeignKey(to='web.ContactGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('nick_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('home_phone', models.CharField(max_length=20)),
                ('office_phone', models.CharField(max_length=20)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('content_modified', models.DateField()),
                ('thumnail_modified', models.DateField()),
                ('image_modified', models.DateField()),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='usercontactgroup',
            name='user_profile',
            field=models.ForeignKey(to='web.UserProfile'),
            preserve_default=True,
        ),
    ]
