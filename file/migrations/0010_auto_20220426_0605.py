# Generated by Django 3.2.12 on 2022-04-26 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0009_rename_airline_id_aircrafts_airline_iata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightrecords',
            name='aircraft_rn',
        ),
        migrations.RemoveField(
            model_name='flightrecords',
            name='flight_number',
        ),
        migrations.RemoveField(
            model_name='flights',
            name='airline_iata',
        ),
        migrations.RemoveField(
            model_name='flights',
            name='destination_icao',
        ),
        migrations.RemoveField(
            model_name='flights',
            name='origin_icao',
        ),
        migrations.RemoveField(
            model_name='records',
            name='email',
        ),
        migrations.RemoveField(
            model_name='records',
            name='flight_id',
        ),
        migrations.DeleteModel(
            name='Aircrafts',
        ),
        migrations.DeleteModel(
            name='Airlines',
        ),
        migrations.DeleteModel(
            name='Airports',
        ),
        migrations.DeleteModel(
            name='FlightRecords',
        ),
        migrations.DeleteModel(
            name='Flights',
        ),
        migrations.DeleteModel(
            name='Records',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
