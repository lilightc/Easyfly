from django.contrib import admin
from file.models import Airports, Airlines, Aircrafts, Flights, FlightRecords, Users, Records, FlightsAirplanes, AirlinePossession, History, Offering, From, To

'''
Django 后台管理系统
网址:laxdata.cuhk.edu.cn/hello/admin/
用户名:admin
密码:admin3170

每次更新完，同样需要运行以下代码对内容进行同步
'cd ./uwsgi/' 
'uwsgi --reload project-master.pid'

可在网站上对数据库进行可视化管理（包括添加数据/删除数据）

'''


admin.site.site_header="Easy Fly Backend Management | 后台可视化管理系统"

def download_csv_airport(modeladmin, request, queryset):
    import csv
    f = open('airport.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["airport_icao", "name","city"])
    for s in queryset:
        writer.writerow([s.airport_icao, s.name,s.city])

class AirportsAdmin(admin.ModelAdmin):
    list_display = ("airport_icao", "name","city")
    action = [download_csv_airport]
admin.site.register(Airports, AirportsAdmin)

def download_csv_airline(modeladmin, request, queryset):
    import csv
    f = open('airline.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["airline_iata","airline_icao", "airline_name"])
    for s in queryset:
        writer.writerow([s.airline_iata, s.airline_icao,s.airline_name])

class AirlinesAdmin(admin.ModelAdmin):
    list_display = ("airline_iata","airline_icao", "airline_name")
    action = [download_csv_airline]
admin.site.register(Airlines, AirlinesAdmin)

def download_csv_aircraft(modeladmin, request, queryset):
    import csv
    f = open('aircraft.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["aircraft_rn","airline_iata","aircraft_type","age","capacity"])
    for s in queryset:
        writer.writerow([s.aircraft_rn, s.airline_iata,s.aircraft_type,s.age,s.capacity])

class AircraftsAdmin(admin.ModelAdmin):
    list_display = ("aircraft_rn","airline_iata","aircraft_type","age","capacity")
    action = [download_csv_aircraft]
admin.site.register(Aircrafts, AircraftsAdmin)

def download_csv_flight(modeladmin, request, queryset):
    import csv
    f = open('flight.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["flight_number", "origin_icao","destination_icao","airline_iata"])
    for s in queryset:
        writer.writerow([s.flight_number, s.origin_icao,s.destination_icao,s.airline_iata])


class FlightsAdmin(admin.ModelAdmin):
    list_display = ("flight_number", "origin_icao","destination_icao","airline_iata")
    action = [download_csv_flight]
admin.site.register(Flights, FlightsAdmin)

def download_csv_flightrecord(modeladmin, request, queryset):
    import csv
    f = open('flightrecord.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["flight_id", "flight_number","departure_time","arrival_time","aircraft_rn","delay"])
    for s in queryset:
        writer.writerow([s.flight_id, s.flight_number,s.departure_time,s.arrival_time, s.aircraft_rn, s.delay])

class FlightRecordsAdmin(admin.ModelAdmin):
    list_display = ("flight_id", "flight_number","departure_time","arrival_time","aircraft_rn","delay")
    action = [download_csv_flightrecord]
admin.site.register(FlightRecords, FlightRecordsAdmin)

def download_csv_user(modeladmin, request, queryset):
    import csv
    f = open('user.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["email", "name","password","gender","age"])
    for s in queryset:
        writer.writerow([s.email, s.name,s.password,s.gender, s.age])

class UsersAdmin(admin.ModelAdmin):
    list_display = ("email", "name","password","gender","age")
    action = [download_csv_user]
admin.site.register(Users, UsersAdmin)

def download_csv_records(modeladmin, request, queryset):
    import csv
    f = open('records.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["email", "flight_id"])
    for s in queryset:
        writer.writerow([s.email, s.flight_id])

class RecordsAdmin(admin.ModelAdmin):
    list_display = ("email", "flight_id")
    action = [download_csv_records]
admin.site.register(Records, RecordsAdmin)
