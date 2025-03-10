from django.db import models

# 每次对数据库进行修改后， 需要运行以下代码：
'''
cd ~/csc3170/ (cd到项目根目录)
python3 manage.py makemigrations     对数据库进行migrate操作
python3 manage.py migrate     
'''

class Airports(models.Model):
    airport_icao = models.CharField(max_length=4, null=False, primary_key=True,verbose_name='机场ICAO代码')
    name = models.CharField(max_length=30, null=False,verbose_name='机场名称')
    city = models.CharField(max_length=30, null=False,verbose_name='机场所在城市')

    class Meta:
        db_table = 'Airports'
        verbose_name = '机场'
        verbose_name_plural = '机场'
        indexes = [models.Index(fields=['airport_icao']), ]

    def __str__(self):  
        return '机场'

class Airlines(models.Model):
    airline_iata = models.CharField(max_length=2, null=False,primary_key=True,verbose_name='航司IATA代码')
    airline_icao = models.CharField(max_length=3,null=False,verbose_name='航司ICAO代码')
    airline_name = models.CharField(max_length=30, null=False,verbose_name='航司名')

    class Meta:
        db_table = 'Airlines'
        verbose_name = '航空公司'
        verbose_name_plural = '航空公司'
        indexes = [models.Index(fields=['airline_iata']), ]

    def __str__(self):  
        return '航空公司'

class Aircrafts(models.Model):
    aircraft_rn = models.CharField(max_length=10,null=False,primary_key=True,verbose_name='飞机注册号')
    airline_iata = models.ForeignKey(Airlines,to_field='airline_iata',on_delete=models.CASCADE,verbose_name='航司IATA代码')
    aircraft_type = models.CharField(max_length=20,verbose_name='机型')
    age = models.IntegerField(null=False,default=0,verbose_name='机龄')
    capacity = models.IntegerField(null=False,default=0,verbose_name='载客量')

    class Meta:
        db_table = 'Aircrafts'
        verbose_name = '飞机'
        verbose_name_plural = '飞机'
        indexes = [models.Index(fields=['aircraft_rn']), ]

    def __str__(self):  
        return '飞机信息'
    
class Flights(models.Model):
    flight_number = models.CharField(max_length=10,null=False,primary_key=True,verbose_name='航班号')
    origin_icao = models.ForeignKey(Airports,to_field='airport_icao',related_name='origin_icao',on_delete=models.CASCADE,verbose_name='出发地机场')
    destination_icao = models.ForeignKey(Airports,to_field='airport_icao',related_name='destination_icao',on_delete=models.CASCADE,verbose_name='目的地机场')
    airline_iata = models.ForeignKey(Airlines,to_field='airline_iata',on_delete=models.CASCADE,verbose_name='航司IATA代码')

    class Meta:
        db_table = 'Flights'
        verbose_name = '航班'
        verbose_name_plural = '航班'
        indexes = [models.Index(fields=['flight_number']), ]

    def __str__(self):  
        return '航班'


class FlightRecords(models.Model):
    flight_id = models.CharField(max_length=10,null=False,primary_key=True,verbose_name='飞行记录ID')
    flight_number = models.ForeignKey(Flights,to_field='flight_number',on_delete=models.CASCADE,verbose_name='航班')
    departure_time = models.CharField(max_length=20,null=False,verbose_name='起飞时间')
    arrival_time = models.CharField(max_length=20,null=False,verbose_name='落地时间')
    aircraft_rn = models.ForeignKey(Aircrafts,to_field='aircraft_rn',on_delete=models.CASCADE,verbose_name='飞机注册号')
    delay = models.CharField(max_length=3,null=False,verbose_name='延误')

    class Meta:
        db_table = 'FlightRecords'
        verbose_name = '飞行记录'
        verbose_name_plural = '飞行记录'

    def __str__(self):  
        return '飞机记录'

class Users(models.Model):
    email = models.CharField(max_length=30, null=False, unique=True, primary_key=True,verbose_name='用户邮箱')
    name = models.CharField(max_length=30, null=False,verbose_name='用户昵称')
    password = models.CharField(max_length=30, null=False, verbose_name='密码')
    gender = models.CharField(max_length=10, null=False, verbose_name='用户性别')
    age = models.IntegerField(null=False, verbose_name='用户年龄')

    class Meta:
        db_table = 'Users'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):  
        return '用户'

class Records(models.Model): #Relationship between Users and FlightRecords
    email = models.ForeignKey(Users,to_field='email',on_delete=models.CASCADE,verbose_name='用户邮箱')
    flight_id = models.ForeignKey(FlightRecords,to_field='flight_id',on_delete=models.CASCADE,verbose_name='飞行记录ID')

    class Meta:
        db_table = 'Records'
        verbose_name = '用户飞行记录'
        verbose_name_plural = '用户飞行记录'

    def __str__(self):  
        return '用户飞行记录'

class FlightsAirplanes(models.Model): #Relationship between Aircrafts and FlightRecords
    aircraft_rn = models.ForeignKey(Aircrafts,to_field='aircraft_rn',on_delete=models.CASCADE,verbose_name='飞机注册号')
    flight_id = models.ForeignKey(FlightRecords,to_field='flight_id',on_delete=models.CASCADE,verbose_name='飞行记录ID')

    class Meta:
        db_table = 'FlightsAirplanes'
        verbose_name = '航班飞机'
        verbose_name_plural = '航班飞机'

    def __str__(self):  
        return '航班飞机'

class AirlinePossession(models.Model): #Relationship between Airlines and Aircrafts
    airline_iata = models.ForeignKey(Airlines,to_field='airline_iata',on_delete=models.CASCADE,verbose_name='航司IATA代码')
    aircraft_rn = models.ForeignKey(Aircrafts,to_field='aircraft_rn',on_delete=models.CASCADE,verbose_name='飞机注册号')

    class Meta:
        db_table = 'AirlinePossession'
        verbose_name = '航司飞机'
        verbose_name_plural = '航司飞机'

    def __str__(self):  
        return '航司飞机'

class History(models.Model): #Relationship between Flights and FlightRecords
    flight_number = models.ForeignKey(Flights,to_field='flight_number',on_delete=models.CASCADE,verbose_name='航班号')
    flight_id = models.ForeignKey(FlightRecords,to_field='flight_id',on_delete=models.CASCADE,verbose_name='飞行记录ID')

    class Meta:
        db_table = 'History'
        verbose_name = '航班历史'
        verbose_name_plural = '航班历史'

    def __str__(self):  
        return '航班历史'

class Offering(models.Model): #Relationship between Flights and Airlines
    airline_iata = models.ForeignKey(Airlines,to_field='airline_iata',on_delete=models.CASCADE,verbose_name='航司IATA代码')
    flight_number = models.ForeignKey(Flights,to_field='flight_number',on_delete=models.CASCADE,verbose_name='航班号')

    class Meta:
        db_table = 'Offering'
        verbose_name = '航司提供航班'
        verbose_name_plural = '航司提供航班'

    def __str__(self):  
        return '航司提供航班'

class From(models.Model): #Relationship between Flights and Airports
    airport_icao = models.ForeignKey(Airports,to_field='airport_icao',on_delete=models.CASCADE,verbose_name='机场ICAO代码')
    flight_number = models.ForeignKey(Flights,to_field='flight_number',on_delete=models.CASCADE,verbose_name='航班号')

    class Meta:
        db_table = 'From'
        verbose_name = '航班起点'
        verbose_name_plural = '航班起点'

    def __str__(self):  
        return '航班起点'

class To(models.Model): #Relationship between Flights and Airports
    airport_icao = models.ForeignKey(Airports,to_field='airport_icao',on_delete=models.CASCADE,verbose_name='机场ICAO代码')
    flight_number = models.ForeignKey(Flights,to_field='flight_number',on_delete=models.CASCADE,verbose_name='航班号')

    class Meta:
        db_table = 'To'
        verbose_name = '航班终点'
        verbose_name_plural = '航班终点'

    def __str__(self):  
        return '航班终点'