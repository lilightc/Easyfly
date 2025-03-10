# Generated by Django 3.2.12 on 2022-04-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightRecords',
            fields=[
                ('flight_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='飞行记录ID')),
                ('delay', models.CharField(max_length=3, verbose_name='延误')),
                ('aircrafts_rn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.aircrafts', verbose_name='飞机注册号')),
            ],
            options={
                'verbose_name': '飞行记录',
                'verbose_name_plural': '飞行记录',
                'db_table': 'FlightRecords',
            },
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('flight_number', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='航班号')),
                ('departure_time', models.DateTimeField(verbose_name='起飞时间')),
                ('arrival_time', models.DateTimeField(verbose_name='落地时间')),
            ],
            options={
                'verbose_name': '航班',
                'verbose_name_plural': '航班',
                'db_table': 'Flight',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '用户飞行记录',
                'verbose_name_plural': '用户飞行记录',
                'db_table': 'Records',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='用户邮箱')),
                ('name', models.CharField(max_length=30, verbose_name='用户昵称')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('gender', models.CharField(max_length=10, verbose_name='用户性别')),
                ('age', models.IntegerField(verbose_name='用户年龄')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'Users',
            },
        ),
        migrations.AlterField(
            model_name='airports',
            name='city',
            field=models.CharField(max_length=30, verbose_name='机场所在城市'),
        ),
        migrations.DeleteModel(
            name='Regions',
        ),
        migrations.AddField(
            model_name='records',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.users', verbose_name='用户邮箱'),
        ),
        migrations.AddField(
            model_name='records',
            name='flight_records',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.flightrecords', verbose_name='飞行记录'),
        ),
        migrations.AddField(
            model_name='flights',
            name='destination_icao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_icao', to='file.airports', verbose_name='目的地机场'),
        ),
        migrations.AddField(
            model_name='flights',
            name='origin_icao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_icao', to='file.airports', verbose_name='出发地机场'),
        ),
        migrations.AddField(
            model_name='flightrecords',
            name='flight_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.flights', verbose_name='航班'),
        ),
    ]
