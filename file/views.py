import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import json, os, requests, random, csv


def hello(request):
    # render在这里可以跳转 /template/目录下的文件，当前设置跳转/template/welcome.html
    # 后续可传参，在{}中加入参数，供前端显示变量
    
    with connection.cursor() as cursor:

        # 所有货机载客量改为0
        # cursor.execute(f"UPDATE Aircrafts SET capacity = 0 where aircraft_type = 'B777F' ")
        # aircraft_list = cursor.fetchall()
        # return HttpResponse(json.dumps(aircraft_list), content_type="application/json")

        # 更改飞机载客量
        # Aircraft_type = "MD90"
        # avg_num = 81
        # cursor.execute(f"SELECT aircraft_rn from aircrafts where aircraft_type = '{Aircraft_type}'")
        # same_aircraft_list = cursor.fetchall()
        # for i in same_aircraft_list:
        #     actual_capacity = random.randint(avg_num-10,avg_num+10)
        #     cursor.execute(f"UPDATE Aircrafts SET capacity = {actual_capacity} where aircraft_rn = '{i[0]}'")
        
        #更改延误率
        # cursor.execute(f"select all flight_id from flightrecords")
        # flight_id_list = cursor.fetchall()
        # target_Status = "yes"
        # change_status_times = 500

        # for i in range(change_status_times):
        #     index_of_list = random.randint(0,6000)
        #     cursor.execute(f"update flightrecords set delay = '{target_Status}' where flight_id = '{flight_id_list[index_of_list][0]}'")
        # cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND (Flights.origin_icao_id='ZYQQ' or Flights.destination_icao_id='ZYQQ')")
        # result=cursor.fetchall()
        # avg_delay_1=result[0][0]
        # cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND (Flights.origin_icao_id='ZYQQ' or Flights.destination_icao_id='ZYQQ') and FlightRecords.delay='yes'")
        # result=cursor.fetchall()
        # avg_delay_2=result[0][0]

        # return HttpResponse(json.dumps({"avg_delay_1":avg_delay_1,"avg_delay_2":avg_delay_2}), content_type="application/json")
        
        # 以CSV文件形式导出sql select结果，下载请访问/hello/
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="delay_rate_versus_x.csv"'},)
        writer = csv.writer(response)
        # 可更改sql正文
        cursor.execute(f"select flightrecords.flight_id, flightrecords.delay, flightrecords.departure_time, flightrecords.arrival_time, \
            aircrafts.age, aircrafts.capacity, aircrafts.airline_iata_id, \
            flights.origin_icao_id, flights.destination_icao_id from flightrecords, flights, aircrafts where \
            flightrecords.flight_number_id = flights.flight_number and flightrecords.aircraft_rn_id = aircrafts.aircraft_rn\
            ")
        result = cursor.fetchall()
        for i in result:
            writer.writerow(i)
        return response

        

    # return redirect("/hello/login_temp/")

def hello2(request):
    return HttpResponse("Hello world!")

'''
测试函数,已在webFile/urls.py中进行网址登记
写完代码之后，用
'cd ./uwsgi/' 
'uwsgi --reload project-master.pid'
两行命令进行外网同步
即可在 laxdata.cuhk.edu.cn/hello/db_test/  实时查看效果

复杂业务函数可以写在views.py外,通过import形式引入本文件

'''

def test_Fetch_Db(request):
    # try:
    with connection.cursor() as cursor:
        # cursor.execute(f'DELETE FROM RECORDS')
        # cursor.execute(f'DELETE FROM FLIGHTRECORDS')
        # cursor.execute(f'DELETE FROM FLIGHTS')
        # cursor.execute(f'DELETE FROM AIRCRAFTS')
        # aircrafts_insertion = "INSERT INTO `Aircrafts` (`aircraft_rn`, `airline_iata_id`, `aircraft_type`,`age`,`capacity`) VALUES"
        # flights_insertion = "INSERT INTO `Flights` (`flight_number`, `origin_icao_id`, `destination_icao_id`,`airline_iata_id`) VALUES"
        # flights_records_insertion = "INSERT INTO `FlightRecords` (`flight_id`, `flight_number_id`, `departure_time`,`arrival_time`,`aircraft_rn_id`,`delay`) VALUES"
        # records_insertion = "INSERT INTO `Records` (`email_id`, `flight_id_id`) VALUES"
        # with open("file/data/aircrafts.txt") as f1:
        #     ts = f1.readlines()
        # for t in ts:
        #     t = t.replace(",\n","")
        #     ins = aircrafts_insertion+t+";"
        #     cursor.execute(ins)
        # f1.close()
        # with open("file/data/flights.txt") as f2:
        #     ts = f2.readlines()
        # for t in ts:
        #     t = t.replace(",\n","")
        #     ins = flights_insertion+t+";"
        #     cursor.execute(ins)
        # f2.close()
        # with open("file/data/flightRecords.txt") as f3:
        #     ts = f3.readlines()
        # for t in ts:
        #     t = t.replace(",\n","")
        #     ins = flights_records_insertion+t+";"
        #     cursor.execute(ins)
        # f3.close()
        # with open("file/data/flightRecords.txt") as f4:
        #      t = f4.read()
        # f4.close()
        # ins = records_insertion+t
        # cursor.execute(ins)


        # cursor.execute(f"Select FlightRecords.aircraft_rn_id, FlightRecords.flight_number_id, FlightRecords.departure_time, \
        #                 FlightRecords.arrival_time, Aircrafts.aircraft_type, FlightRecords.delay, flights.origin_icao_id, \
        #                 flights.destination_icao_id From FlightRecords, flights, aircrafts \
        #                 where flights.flight_number = FlightRecords.flight_number_id AND\
        #                 aircrafts.aircraft_rn = FlightRecords.aircraft_rn_id AND FlightRecords.flight_id in \
        #                 (SELECT flight_id_id FROM records where email_id = '130000005@link.cuhk.edu.cn')")
        
        cursor.execute(f"select * from flights where flight_number = 'SC6055'")
        result1 = cursor.fetchall()
        cursor.execute(f"select * from aircrafts where aircraft_rn = 'B-8811'")
        result2 = cursor.fetchall()
        cursor.execute(f"select * from flightrecords where flight_number_id = 'SC6055'")
        result3 = cursor.fetchall()
        return_dict = {"status":"Success","result1":result1,"result2":result2,"result3":result3}
        
        # 对错误航班号进行更新（已完成）
        # cursor.execute(f"select flight_number from flights")
        # result = cursor.fetchall()
        # for i in result:
        #     flight_number = i[0]
        #     iata_nums =i[0][0:2]
        #     cursor.execute(f"UPDATE Flights SET airline_iata_id = '{iata_nums}' where flight_number = '{flight_number}'")
        
        # 对错误飞行记录关系进行更新（已完成）
        '''
        cursor.execute(f"select flight_id, flight_number_id from flightrecords")
        flight_id_list = cursor.fetchall()
        for i in flight_id_list:
            flight_id = i[0]
            flight_number = i[1]
            airline_iata = flight_number[0:2]
            cursor.execute(f"select aircraft_rn from aircrafts where airline_iata_id = '{airline_iata}'")
            airline_aircraft_list = cursor.fetchall()
            aircraft_rn_actual = random.choice(airline_aircraft_list)
            cursor.execute(f"UPDATE Flightrecords SET aircraft_rn_id = '{aircraft_rn_actual[0]}' where flight_id = '{flight_id}'")
        
        # cursor.execute(f"select aircraft_rn_id, flight_number_id from flightrecords")
        # rn_list = cursor.fetchall()
        return_dict = {"result":"Succcess"}
        '''
        '''
        方法2:
        cursor = connection.cursor()
        ...
        '''
    # except:
    #     msg = "Failed"
    #     return_dict = {"status":"Success","Hint":msg}
    return HttpResponse(json.dumps(return_dict), content_type="application/json")

# def data_insertion(request):
#     try:
#         with connection.cursor() as cursor:
#             data_loading(cursor)
#             msg = cursor.fetchall()
#             return_dict = {"status":"Success","result":msg}
#     except:
#         msg = "Failed"
#         return_dict = {"status":"Success","Hint":msg}
#     return HttpResponse(json.dumps(return_dict), content_type="application/json")

def login_temp(request): #done (doesn't need to be modified)
    if 'password' in request.session:
        return redirect("/hello/search_page")

    if request.method == 'POST':
        email = request.POST.get("username")
        password = request.POST.get("password")
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT EMAIL, PASSWORD FROM USERS")
            result = cursor.fetchall()
            if (email, password) in result:
                cursor.execute(f"SELECT NAME, GENDER, AGE FROM USERS WHERE email = '{email}'")
                name, gender, age = cursor.fetchall()[0]
                request.session['email'] = email
                request.session['password'] = password
                request.session['username'] = name
                request.session['gender'] = gender
                request.session['age'] = age
                
                return render(request, "search_page.html", {}) #改成学妹的主页面url
            else:
                return render(request, "login_temp.html", {"error_message": "Invalid email or password."})
    else:
        return render(request, "login_temp.html")

def signUp(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            gender = request.POST.get("gender")
            # if(request.POST.get("gender1",None) == "on"):
            #     gender = "Male"
            # elif(request.POST.get("gender2",None) == "on"):
            #     gender = "Female"
            # else:
            #     gender = "Others"
            age = request.POST.get("age")
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT email from USERS")
                result= cursor.fetchall()
                if(email) in result:
                    return render(request, "signUp.html",{"error_message":"username already exists!"})
                else:
                    cursor.execute(f"INSERT OR FAIL INTO USERS VALUES('{email}','{username}','{password}','{gender}',{age})")
                    connection.commit()
                    request.session['email'] = email
                    request.session['password'] = password
                    request.session['username'] = username
                    request.session['gender'] = gender
                    request.session['age'] = age
                    return render(request, "search_page.html",{})
        except:
            return render(request, "signUp.html", {"error_message": "Invalid Sign-up information! Please try again."})
    else:
        return HttpResponse("Not in POST method.")


#aircarftDict的键值？

# def aircraftJump(request):
#     if request.method == 'GET':
#         if 'model' in request.GET:
#             model=request.GET['model']
#             with connection.cursor() as cursor:
#                 result = cursor.execute(f"SELECT aircraft_type, aircraft_rn, airline_iata, age, capacity FROM Aircrafts WHERE aircraft_type=%s",[model])
#                 if(result==[]):
#                     return render(request,"aircraftJump.html",{"error_message":"No such model!"})
#                 else:
#                     for row in result: #aircarftDict的键值？
#                         return render(request)        
#     return render(request)

# def airportJump(request):
#    if request.method == 'GET':
#        if 'icao' in request.GET:
#            icao=request.GET['icao']
#            with connection.cursor() as cursor:
#                result = cursor.execute(f"SELECT airport_icao, name, city FROM Airports WHERE aircraft_icao=%s",[icao])
#                if(result==[]):
#                    return render(request,"airportJump.html",{"error_message":"No such airport!"})
#                else:#根据icao查询结果应只有一个
#                    result_icao = result[0][0]
#                    result_name = result[0][1]
#                    result_city = result[0][2]
#                    airport_dict = {'icao':result_icao,'name':result_name,'city':result_city}
#                    return render(request,'airportJump.html',{'airportDict':airport_dict})   
#    return render(request)


# def airlineJump(request):
    # if request.method == 'GET':
    #     if 'iata' in request.GET:
    #         iata=request.GET['iata']
    #         with connection.cursor() as cursor:
    #             result = cursor.execute(f"SELECT airline_iata, airline_icao, airline_name FROM Airlines WHERE airline_iata=%s",[iata])
    #             if(result==[]):
    #                 return render(request,"airlineJump.html",{"error_message":"No such airline!"})
    #             else:
    #                 for row in result: 
    #                     return render(request)        
    # return render(request)


def airline(request):
    if request.method == 'POST':
        search_by = request.POST.get("Search_by")
        if (search_by == "IATA"):
            with connection.cursor() as cursor:
                airline_query = request.POST.get("searchAirline")
                cursor.execute(f"SELECT * from airlines where airline_iata like '%{airline_query}%'order by airline_name")
                result = cursor.fetchall()
                airlines=[]
                for row in result:
                    item={}
                    item['airline_name']=row[2]
                    item['content']=row[0]
                    item['airline_iata']=row[0]
                    airlines.append(item)
                return render(request, 'airline.html',{'airline':airlines})
        elif (search_by == "ICAO"):
            with connection.cursor() as cursor:
                airline_query = request.POST.get("searchAirline")
                cursor.execute(f"SELECT * from airlines where airline_icao like '%{airline_query}%'order by airline_name")
                result = cursor.fetchall()
                airlines=[]
                for row in result:
                    item={}
                    item['airline_name']=row[2]
                    item['content']=row[1]
                    item['airline_iata']=row[0]
                    airlines.append(item)
                return render(request, 'airline.html',{'airline':airlines})
        else:
            with connection.cursor() as cursor:
                airline_query = request.POST.get("searchAirline")
                cursor.execute(f"SELECT * from airlines where airline_name like '%{airline_query}%'order by airline_name")
                result = cursor.fetchall()
                airlines=[]
                for row in result:
                    item={}
                    item['airline_name']=row[2]
                    item['airline_iata']=row[0]
                    airlines.append(item)
                return render(request, 'airline.html',{'airline':airlines})


        # 按IATA关键字查询
        # if(request.POST.get("Search_by_IATA",None) == "on"):
        #     with connection.cursor() as cursor:
        #         airline_query = request.POST.get("searchAirline")
        #         cursor.execute(f"SELECT * from airlines where airline_iata like '%{airline_query}%'order by airline_name")
        #         result = cursor.fetchall()
        #         airlines=[]
        #         for row in result:
        #             item={}
        #             item['airline_name']=row[2]
        #             item['content']=row[0]
        #             item['airline_iata']=row[0]
        #             airlines.append(item)
        #         return render(request, 'airline.html',{'airline':airlines})
        # # 按ICAO关键字查询
        # elif(request.POST.get("Search_by_ICAO",None) == "on"):
        #     with connection.cursor() as cursor:
        #         airline_query = request.POST.get("searchAirline")
        #         cursor.execute(f"SELECT * from airlines where airline_icao like '%{airline_query}%'order by airline_name")
        #         result = cursor.fetchall()
        #         airlines=[]
        #         for row in result:
        #             item={}
        #             item['airline_name']=row[2]
        #             item['content']=row[1]
        #             item['airline_iata']=row[0]
        #             airlines.append(item)
        #         return render(request, 'airline.html',{'airline':airlines})
        # # 按航司名称查询(默认)
        # else:
        #     with connection.cursor() as cursor:
        #         airline_query = request.POST.get("searchAirline")
        #         cursor.execute(f"SELECT * from airlines where airline_name like '%{airline_query}%'order by airline_name")
        #         result = cursor.fetchall()
        #         airlines=[]
        #         for row in result:
        #             item={}
        #             item['airline_name']=row[2]
        #             item['airline_iata']=row[0]
        #             airlines.append(item)
        #         return render(request, 'airline.html',{'airline':airlines})
        # 按延误率搜索（order by asc)(待完成)

    # 通过GET方法，第一次访问该网址，默认获取所有航司列表
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from airlines order by airline_name")
            result = cursor.fetchall()
            airlines=[]
            for row in result:
                item={}
                item['airline_name']=row[2]
                item['airline_iata']=row[0]
                airlines.append(item)
            return render(request, 'airline.html',{'airline':airlines})

def airport(request):
    if request.method == 'POST':
        search_by = request.POST.get("Search_by")
        if (search_by == "CITY"):
            with connection.cursor() as cursor:
                airport_query = request.POST.get("searchAirport")
                cursor.execute(f"SELECT * from airports where city like '%{airport_query}%' Order by name")
                result = cursor.fetchall()
                airports=[]
                for i in range(len(result)):
                    item={}
                    item['airport_icao']=result[i][0]
                    item['name']=result[i][1]
                    item['content']=result[i][2]
                    airports.append(item)
                return render(request, 'airport.html',{'airport':airports})
        elif (search_by == "ICAO"):
            with connection.cursor() as cursor:
                airport_query = request.POST.get("searchAirport")
                cursor.execute(f"SELECT * from airports where airport_icao like '%{airport_query}%' Order by name")
                result = cursor.fetchall()
                airports=[]
                for i in range(len(result)):
                    item={}
                    item['airport_icao']=result[i][0]
                    item['content']=result[i][0]
                    item['name']=result[i][1]
                    airports.append(item)
                return render(request, 'airport.html',{'airport':airports})
        else:
            with connection.cursor() as cursor:
                airport_query = request.POST.get("searchAirport")
                cursor.execute(f"SELECT * from airports where name like '%{airport_query}%' Order by name")
                result = cursor.fetchall()
                airports=[]
                for i in range(len(result)):
                    item={}
                    item['airport_icao']=result[i][0]
                    item['name']=result[i][1]
                    airports.append(item)
                return render(request, 'airport.html',{'airport':airports})

        # 通过城市搜索机场
        # if(request.POST.get("Search_by_CITY",None) == "on"):
        #     with connection.cursor() as cursor:
        #         airport_query = request.POST.get("searchAirport")
        #         cursor.execute(f"SELECT * from airports where city like '%{airport_query}%' Order by name")
        #         result = cursor.fetchall()
        #         airports=[]
        #         for i in range(len(result)):
        #             item={}
        #             item['airport_icao']=result[i][0]
        #             item['name']=result[i][1]
        #             item['content']=result[i][2]
        #             airports.append(item)
        #         return render(request, 'airport.html',{'airport':airports})
        # # 通过ICAO代码搜索
        # elif(request.POST.get("Search_by_ICAO",None) == "on"):
        #     with connection.cursor() as cursor:
        #         airport_query = request.POST.get("searchAirport")
        #         cursor.execute(f"SELECT * from airports where airport_icao like '%{airport_query}%' Order by name")
        #         result = cursor.fetchall()
        #         airports=[]
        #         for i in range(len(result)):
        #             item={}
        #             item['airport_icao']=result[i][0]
        #             item['content']=result[i][0]
        #             item['name']=result[i][1]
        #             airports.append(item)
        #         return render(request, 'airport.html',{'airport':airports})
        # # 通过机场名称搜索（默认）
        # else:
        #     with connection.cursor() as cursor:
        #         airport_query = request.POST.get("searchAirport")
        #         cursor.execute(f"SELECT * from airports where name like '%{airport_query}%' Order by name")
        #         result = cursor.fetchall()
        #         airports=[]
        #         for i in range(len(result)):
        #             item={}
        #             item['airport_icao']=result[i][0]
        #             item['name']=result[i][1]
        #             airports.append(item)
        #         return render(request, 'airport.html',{'airport':airports})
    # 通过GET方法，第一次访问该网址，默认获取所有机场列表
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from airports Order by name")
            result = cursor.fetchall()
            airports=[]
            for i in range(len(result)):
                item={}
                item['airport_icao']=result[i][0]
                item['name']=result[i][1]
                item['city']=result[i][2]
                airports.append(item)
            return render(request, 'airport.html',{'airport':airports})

def aircraft(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            aircraft_query = request.POST.get("searchAircraft")
            cursor.execute(f"SELECT aircraft_rn, airline_iata_id, aircraft_type, age, capacity, count(distinct aircraft_type) from aircrafts where aircraft_type like '%{aircraft_query}%' Group by aircraft_type Order by aircraft_type")
            result = cursor.fetchall()
            aircrafts=[]
            for row in result:
                item={}
                item['aircraft_rn']=row[0]
                item['airline_iata']=row[1] 
                item['aircraft_type']=row[2]
                item['age']=row[2]
                item['capacity']=row[3]
                aircrafts.append(item)
            return render(request, 'aircraft.html',{'aircraft':aircrafts})
            
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT aircraft_rn, airline_iata_id, aircraft_type, age, capacity, count(distinct aircraft_type) from aircrafts Group by aircraft_type Order by aircraft_type")
            result = cursor.fetchall()
            # cursor.execute(f"SELECT ")
            aircrafts=[]
            for row in result:
                item={}
                item['aircraft_rn']=row[0]
                item['airline_iata']=row[1] 
                item['aircraft_type']=row[2]
                item['age']=row[2]
                item['capacity']=row[3]
                aircrafts.append(item)
            return render(request, 'aircraft.html',{'aircraft':aircrafts})

def airlineJump(request, airline_iata):
    '''
    重要！
    当使用sql select 数据库,而所选column为foreign key时,
    要在该行后加上"_id"才能被执行
    如 airline_Data 这一列为foreign key,
    那么我们sql中应该这样写,SELECT airline_Data_id from ...
    '''

    # #Example: 用ORM实现
    # from file.models import Airlines, Aircrafts
    # from django.db.models import F 
    # airline = Airlines.objects.get(airline_iata = airline_iata)
    # dict_airlineJump = {}
    # dict_airlineJump['iata'] = airline.airline_iata
    # dict_airlineJump['icao'] = airline.airline_icao
    # dict_airlineJump['name'] = airline.airline_name

    # aircraft = Aircrafts.objects.filter(airline_iata = airline_iata) 
    # dict_airlineJump['aircraft'] = aircraft
    # return render(request, 'airlineJump.html', dict_airlineJump)
    
    # Actual: 用SQL实现
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from airlines where airline_iata = '{airline_iata}'")
        airlines_detail= cursor.fetchall()
        cursor.execute(f"SELECT aircraft_rn, airline_iata_id, aircraft_type, age, capacity from aircrafts where airline_iata_id = '{airline_iata}'")
        aircraft_list = cursor.fetchall()
        aircraft_result = []
        for i in aircraft_list:
            single_aircraft = {}
            single_aircraft['aircraft_rn'] = i[0]
            single_aircraft['airline_iata'] = i[1]
            single_aircraft['aircraft_type'] = i[2]
            single_aircraft['age'] = i[3]
            if(i[4] == 0.0):
                single_aircraft['capacity'] = "Cargo"
            else:
                single_aircraft['capacity'] = i[4]
            aircraft_result.append(single_aircraft)
        cursor.execute(f"SELECT aircraft_type, count(*) from aircrafts where airline_iata_id='{airline_iata}' group by aircraft_type order by count(*) desc")
        result = cursor.fetchall()
        aircraft_type_1=result[0][0]
        aircraft_type_2=result[1][0]
        aircraft_type_3=result[2][0]
        type_1_own=result[0][1]
        type_2_own=result[1][1]
        type_3_own=result[2][1]
        cursor.execute(f"SELECT origin_icao_id,count(*) from Flights where airline_iata_id='{airline_iata}' group by origin_icao_id order by count(*) desc")
        result=cursor.fetchall()
        most_depature_airport=result[0][0]
        cursor.execute(f"SELECT destination_icao_id,count(*) from Flights where airline_iata_id='{airline_iata}' group by destination_icao_id order by count(*) desc")
        result=cursor.fetchall()
        most_destination_airport=result[0][0]
        cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND (Flights.airline_iata_id='{airline_iata}')")
        result=cursor.fetchall()
        avg_delay=result[0][0]
        cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND Flights.airline_iata_id='{airline_iata}' and FlightRecords.delay='yes'")
        result=cursor.fetchall()
        avg_delay=round(result[0][0]/avg_delay,2)
        return render(request, 'airlineJump.html',{'iata':airline_iata, 'icao':airlines_detail[0][1], 'name':airlines_detail[0][2], 'aircraft':aircraft_result,
        'aircraft_type_1':aircraft_type_1,'aircraft_type_2':aircraft_type_2,'aircraft_type_3':aircraft_type_3,'type_1_own':type_1_own,'type_2_own':type_2_own,'type_3_own':type_3_own,'most_depature_airport':most_depature_airport,'most_destination_airport':most_destination_airport,'avg_delay':avg_delay})

def airportJump(request, airport_icao):
    # from file.models import Airports
    # airport = Airports.objects.get(airport_icao = airport_icao)
    # dict_airportJump = {}
    # dict_airportJump['airport_icao'] = airport_icao
    # dict_airportJump['name'] = airport.name
    # dict_airportJump['city'] = airport.city
    # return render(request, 'airportJump.html', dict_airportJump)

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from airports where airport_icao = '{airport_icao}'")
        airport_result= cursor.fetchall()

        # airport_result = []
        # for row in airport_result:
        #     item={}
        #     item['airport_icao']=row[0]
        #     item['name']=row[1]
        #     item['city']=row[2]
        #     airport_result.append(item)
        cursor.execute(f"SELECT airline_iata_id, count(*) from Flights join FlightRecords where Flights.origin_icao_id='{airport_icao}' or Flights.destination_icao_id='{airport_icao}' group by airline_iata_id order by count(*) desc")
        result=cursor.fetchall()
        airline_1=result[0][0]
        airline_2=result[1][0]
        airline_3=result[2][0]
        cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND (Flights.origin_icao_id='{airport_icao}' or Flights.destination_icao_id='{airport_icao}')")
        result=cursor.fetchall()
        avg_delay=result[0][0]
        cursor.execute(f"SELECT count(*) from Flights join FlightRecords where (Flights.flight_number = FlightRecords.flight_number_id) AND (Flights.origin_icao_id='{airport_icao}' or Flights.destination_icao_id='{airport_icao}') and FlightRecords.delay='yes'")
        result=cursor.fetchall()
        avg_delay=round(result[0][0]/avg_delay,2)
        # avg_delay=result[0][0]
        return render(request, 'airportJump.html',{'airport_icao':airport_result[0][0],'name':airport_result[0][1],'city':airport_result[0][2],'avg_delay':avg_delay,'airline_1':airline_1,'airline_2':airline_2,'airline_3':airline_3})

def aircraftJump(request, model):
    with connection.cursor() as cursor:
        # cursor.execute(f"SELECT * from airports where airport_icao = '{airport_icao}'")
        cursor.execute(f"SELECT aircraft_rn, airline_iata_id, aircraft_type, age, capacity from aircrafts where aircraft_type = '{model}' Order by aircraft_type")
        result= cursor.fetchall()
        aircraft_result = []
        for row in result:
            item={}
            item['aircraft_rn']=row[0]
            item['airline_iata']=row[1]
            # item['aircraft_type']=row[2]
            item['age']=row[3]
            if(row[4] == 0.0):
                item['capacity']="Cargo"
            else:
                item['capacity']=row[4]
            aircraft_result.append(item)
        cursor.execute(f"SELECT avg(age) from aircrafts where aircraft_type='{model}'")
        result=cursor.fetchall()
        avg_age = result[0][0]
        avg_age = round(avg_age,2)
        cursor.execute(f"SELECT avg(capacity) from aircrafts where aircraft_type='{model}'")
        result=cursor.fetchall()
        avg_capacity = result[0][0]
        avg_capacity = round(avg_capacity,2)
        if(avg_capacity == 0.0):
            avg_capacity = "Cargo"
        cursor.execute(f"SELECT airline_iata_id, count(*) from aircrafts where aircraft_type='{model}' group by airline_iata_id order by count(*) desc")
        result=cursor.fetchall()
        airline_1=result[0][0]
        airline_1_own=result[0][1]
        airline_2=result[1][0]
        airline_2_own=result[1][1]
        airline_3=result[2][0]
        airline_3_own=result[2][1]
        return render(request, 'aircraftJump.html',{'aircraft_type':model,'aircraft':aircraft_result,'avg_age':avg_age,'avg_capacity':avg_capacity,'airline_1':airline_1,'airline_1_own':airline_1_own,'airline_2':airline_2,'airline_2_own':airline_2_own,'airline_3':airline_3,'airline_3_own':airline_3_own})

def testjump(request):
    index = request.GET.get('index')
    print('index =', index)
    return render(request, "testjump.html", {"message": "test"})

def test(request):
    return render(request, "test.html")

def search_page(request):
    if 'password' not in request.session:
        return redirect("/hello/login_temp/")
    return render(request, "search_page.html")

def search_result(request):
    if 'password' not in request.session:
        return redirect("/hello/login_temp/")

    # 暂时供前端测试使用
    # result = {}
    # result["airline_iata"] = "AC"
    # result["flight_number"] = "AC3030"
    # result["departure"] = "VHHH"
    # result["destination"] = "VCZH"
    # result["departure_time"] = "20202020"
    # result["arrival_time"] = "20202021"
    # result["aircraft_type"] = "B777-300ER"
    # result["delay"] = "no"
    # outcome = [result]
    # outcome = []


    # return render(request,'search_page.html',{'flight_history':outcome,'status':"True"}) #传参待定

    # 凑SQL方法：检测不同表单是否有值，并据此采取不同的SQL搜索策略（共2^5 = 32种）
    # 可以优化搜索效率（亮点）
    s_airline=request.POST.get("s_airline")
    s_model=request.POST.get("s_model")
    s_origin=request.POST.get("s_origin")
    s_destination=request.POST.get("s_destination")
    s_no=request.POST.get("s_no")
    if ((s_airline!='') or (s_model!='') or (s_origin!='') or (s_destination!='') or (s_no!='')):
        with connection.cursor() as cursor:
            history=[]

            if(s_airline!=''):
                cursor.execute(f"CREATE TEMP TABLE v_airline as \
                                    Select * from Airlines where airline_iata='{s_airline}'")
            else:
                cursor.execute(f"CREATE TEMP TABLE v_airline as \
                                    Select * from Airlines")

            if(s_model!=''):
                cursor.execute(f"CREATE TEMP TABLE v_aircraft as \
                                    Select aircraft_rn, airline_iata_id, aircraft_type from Aircrafts where aircraft_type='{s_model}'")
            else:
                cursor.execute(f"CREATE TEMP TABLE v_aircraft as \
                                    Select aircraft_rn, airline_iata_id, aircraft_type from Aircrafts")
            
            if(s_origin!=''):
                cursor.execute(f"CREATE TEMP TABLE v_origin as \
                                    Select airport_icao as origin_icao from Airports where airport_icao='{s_origin}'")
            else:
                cursor.execute(f"CREATE TEMP TABLE v_origin as \
                                    Select airport_icao as origin_icao from Airports")

            if(s_destination!=''):
                cursor.execute(f"CREATE TEMP TABLE v_destination as \
                                    Select airport_icao as destination_icao from Airports where airport_icao='{s_destination}'")
            else:
                cursor.execute(f"CREATE TEMP TABLE v_destination as \
                                    Select airport_icao as destination_icao from Airports")       

            if(s_no!=''):
                cursor.execute(f"CREATE TEMP TABLE v_no as \
                                    Select flight_number, origin_icao_id, destination_icao_id, airline_iata_id \
                                        from Flights where flight_number='{s_no}'")
            else:
                cursor.execute(f"CREATE TEMP TABLE v_no as \
                                    Select flight_number, origin_icao_id, destination_icao_id, airline_iata_id \
                                        from Flights")
            
            cursor.execute(f"CREATE TEMP TABLE flight_info as \
                                Select flight_number, origin_icao_id, destination_icao_id, airline_iata_id, \
                                        departure_time, arrival_time, aircraft_rn_id, delay \
                                    from v_no JOIN FlightRecords ON v_no.flight_number=FlightRecords.flight_number_id")
            cursor.execute(f"CREATE TEMP TABLE with_airline as \
                                Select flight_number, origin_icao_id, destination_icao_id, airline_iata, departure_time, arrival_time, aircraft_rn_id, delay \
                                    from flight_info JOIN v_airline ON v_airline.airline_iata=flight_info.airline_iata_id")
            cursor.execute(f"CREATE TEMP TABLE with_aircraft as \
                                Select flight_number, origin_icao_id, destination_icao_id, airline_iata, departure_time, arrival_time, aircraft_type, delay \
                                    from with_airline JOIN v_aircraft ON with_airline.aircraft_rn_id=v_aircraft.aircraft_rn")
            cursor.execute(f"CREATE TEMP TABLE with_origin as \
                                Select flight_number, origin_icao, destination_icao_id, airline_iata, departure_time, arrival_time, aircraft_type, delay \
                                    from with_aircraft JOIN v_origin ON with_aircraft.origin_icao_id=v_origin.origin_icao")
            cursor.execute(f"CREATE TEMP TABLE with_destination as \
                                Select flight_number, origin_icao, destination_icao, airline_iata, departure_time, arrival_time, aircraft_type, delay \
                                    from with_origin JOIN v_destination ON with_origin.destination_icao_id=v_destination.destination_icao")
            cursor.execute(f"Select * from with_destination")
            result=cursor.fetchall()
            for i in result:
                item={}
                item['flight_number']=i[0]
                item['departure']=i[1]
                item['destination']=i[2]
                item['airline_iata']=i[3]
                item['departure_time']=i[4]
                item['arrival_time']=i[5]
                item['aircraft_type']=i[6]
                item['delay']=i[7]
                history.append(item)
            return render(request,'search_page.html',{'flight_history':history,'status':True}) #传参待定
    else:
        history=[]
        return render(request,'search_page.html',{'flight_history':history,'status':True})

def user(request):
    if 'password' not in request.session:
        return redirect("/hello/login_temp/")
    with connection.cursor() as cursor:

        msg = "step 1"
        cursor.execute(f"Select aircrafts.airline_iata_id, FlightRecords.flight_number_id, FlightRecords.departure_time, \
                        FlightRecords.arrival_time, Aircrafts.aircraft_type, FlightRecords.delay, flights.origin_icao_id, \
                        flights.destination_icao_id From FlightRecords, flights, aircrafts \
                        where flights.flight_number = FlightRecords.flight_number_id AND\
                        aircrafts.aircraft_rn = FlightRecords.aircraft_rn_id AND FlightRecords.flight_id in \
                        (SELECT flight_id_id FROM records where email_id = '{request.session['email']}')\
                        ORDER BY FlightRecords.arrival_time DESC")
        result = cursor.fetchall()
        return_list = []
        msg = "step 2"
        print("Yes")
        for row in result:
            if row[4][-1]!='F':
                i={}
                i['airline_iata'] = row[0]
                i['flight_number'] = row[1]
                i['departure_time'] = row[2]
                i['arrival_time'] = row[3]
                i['aircraft_type'] = row[4]
                i['delay'] = row[5]
                i['departure'] = row[6]
                i['destination'] = row[7]
                return_list.append(i)
        msg = return_list
        print("Yes")
        return render(request, "user.html", {"email":request.session['email'],
                    "password":request.session['password'],
                    "username":request.session['username'],
                    "gender":request.session['gender'],
                    "age":request.session['age'],
                    "flight_history":return_list})


def signUp_page(request):
    return render(request, "signUp.html")

def logout(request):
    if 'password' in request.session:
        del request.session['password']
        return redirect("/hello/login_temp/")

def prediction(request): #TODO: data analysis 等待补全
    return render(request, "prediction.html")