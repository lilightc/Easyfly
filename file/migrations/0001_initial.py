# Generated by Django 3.2.12 on 2022-04-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, verbose_name='Test_name')),
                ('test_id', models.CharField(max_length=99, verbose_name='Test_id')),
            ],
            options={
                'verbose_name': '测试数据库',
                'verbose_name_plural': '测试数据库',
                'db_table': 'Tests',
            },
        ),
    ]
