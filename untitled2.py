# -*- coding: utf-8 -*-
# -*- coding: cp949 -*-
import urllib.request
import xml.etree.ElementTree as etree

loopFlag = 1
subwayFlag = 1

#--------------------------------지하철 전채 첫/막차 시간--------------------------------------------------------------
def subway(End, Line, Day, Inout):
    key = "704645626873646b313979416f7257"
    url = "http://openAPI.seoul.go.kr:8088/"+key+"/xml/SearchFirstAndLastTrainInfobyLineService/1/" + End + "/" + Line + "/" + Day + "/" + Inout + "/"
    
    data = urllib.request.urlopen(url).read()

    filename = "subway.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("row")
    print("외부코드\t전철역코드\t전철역\t첫차시간\t첫차출발역\t막차시간\t막차출발역\t막차도착역")
    for item in itemElements:
        FR_CODE = item.find("FR_CODE")                   #외부코드
        STATION_CD = item.find("STATION_CD")             #전철역코드
        STATION_NM = item.find("STATION_NM")             #전철역명
        FIRST_TIME = item.find("FIRST_TIME")             #첫차시간
        F_SUBWAYSNAME = item.find("F_SUBWAYSNAME")       #첫차출발역명
        LAST_TIME = item.find("LAST_TIME")               #막차시간
        L_SUBWAYSNAME = item.find("L_SUBWAYSNAME")       #막차출발역명
        L_SUBWAYENAME = item.find("L_SUBWAYENAME")       #막차도착역명
            
        print(str(FR_CODE.text) + "\t" + str(STATION_CD.text)+  "\t" + str(STATION_NM.text)
        + "\t" + str(FIRST_TIME.text) + "\t" + str(F_SUBWAYSNAME.text) + "\t" + str(LAST_TIME.text)  
        + "\t" + str(L_SUBWAYSNAME.text) + "\t" + str(L_SUBWAYENAME.text))
        
    mail = input("메일? y/n ")
    if mail == 'y':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept, filename)
    elif mail == 'n':
            print("ok....")
    
#---------------------------------지하철역막차검색----------------------------------------------------------------
def subwaySearch(Code, Day, Inout):
    key = "4357414e6f73646b3132397643534a4b"
    url = "http://openAPI.seoul.go.kr:8088/" + key + "/xml/SearchLastTrainTimeByIDService/1/10/" + Code + "/" + Day +"/" + Inout + "/"
    
    data = urllib.request.urlopen(url).read()

    filename = "subway.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("row")
    print("외부코드\t전철역코드\t전철역\t종착역명\t출발시간")
    for item in itemElements:
        #if(item.find("infoType")).text == "1":
        FR_CODE = item.find("FR_CODE")                   #외부코드
        STATION_CD = item.find("STATION_CD")             #전철역코드
        STATION_NM = item.find("STATION_NM")             #전철역명
        SUBWAYENAME = item.find("SUBWAYENAME")         #종착역명
        LEFTTIME = item.find("LEFTTIME")                 #출발시간
            
        print(str(FR_CODE.text) + "\t" + str(STATION_CD.text)+  "\t" + str(STATION_NM.text) + "\t" + str(SUBWAYENAME.text) + "\t" + str(LEFTTIME.text))
        
    mail = input("메일? y/n ")
    if mail == 'y':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept, filename)
    elif mail == 'n':
            print("ok....")
#-------------------------------------------------------------------------------------------
#-------------------------------------한글 utf-8 변환후 바꾸기----------------------------------
def Change(Name):
    Name = Name.replace("b", "", 1)
    Name = Name.replace("'", "")
    Name = Name.replace("\\x", "%")
    
    subwayMakeaSearch(Name)
#-----------------------------------역 검색해서 찾기----------------------------------------
def subwayMakeaSearch(StationName):
    key = "GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D"
    url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getKwrdFndSubwaySttnList?ServiceKey=" + key + "&subwayStationName=" + StationName
    
    data = urllib.request.urlopen(url).read()

    filename = "subwayMakeaSearch.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("역코드\t역이름")
    for item in itemElements:
        #if(item.find("infoType")).text == "1":
        subwaystationid = item.find("subwaystationid")                 #역코드
        subwaystationname = item.find("subwaystationname")             #역이름
            
        print(str(subwaystationid.text) + "\t" + str(subwaystationname.text) )
    global subwayFlag
    while (subwayFlag > 0):    
        print("\n")
        print("===Select Menu===")
        print("막차검색:  l")
        print("전체시간표검색: f")
        print("출구별 역주변 시설보기: a")
        print("출구별 버스: b")
        print("나가기: q")
        print("=================")
        subwayKey = str(input ('select menu :'))
        subwayMenuFun(subwayKey)
    
    subwayFlag = 1
#---------------------------------역 검색 후 메뉴기능-------------------------------------
def subwayMenuFun(menu):
    if menu == 'l':
        Code = input("검색할 역코드를 입력하세요(SES제외): ")
        Day = input("요일(평:1, 토: 2, 일/공: 3): ")
        Inout = input("상(1)/하(2))행선: ")
        subwaySearch(Code, Day, Inout)
    elif menu == 'f':
        Code = input("검색할 역코드를 입력하세요: ")
        Day = input("요일(평:1, 토: 2, 일/공: 3): ")
        Inout = input("상(U)/하(D))행선: ")
        subwayFull(Code, Day, Inout)
    elif menu == 'a':
        Code = input("검색할 역코드를 입력하세요: ")
        subwayAround(Code)
    elif menu == 'b':
        Code = input("검색할 역코드를 입력하세요: ")
        subwayBus(Code)
    elif menu == 'q':
        global subwayFlag
        subwayFlag = 0
    else:
        print("error!")
    
#------------------------------------역 검색 후 전체시간표--------------------------------
def subwayFull(Code, Day, InOut):
    key = "GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D"
    url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList?ServiceKey=" + key + "&subwayStationId=" + Code + "&dailyTypeCode=0" + Day + "&upDownTypeCode=" + InOut + "&numOfRows=999&pageSize=999&pageNo=1&startPage=1"
    
    data = urllib.request.urlopen(url).read()

    filename = "subwayFull.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("도착시간\t종점역이름")
    for item in itemElements:
        arrtime = item.find("arrtime")                   #도착시간
        endsubwaystationnm = item.find("endsubwaystationnm")             #종점역이름
            
        print(str(arrtime.text) + "\t" + str(endsubwaystationnm.text))
    
    mail = input("메일? y/n ")
    if mail == 'y':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept, filename)
    elif mail == 'n':
            print("ok....")

        
#---------------------------------------역 출구별 건물--------------------------------------
def subwayAround(Code):
    key = "GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D"
    url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnExitAcctoCfrFcltyList?ServiceKey=" + key + "&subwayStationId=" + Code + "&numOfRows=999&pageSize=999&pageNo=1&startPage=1"
    
    data = urllib.request.urlopen(url).read()

    filename = "subwayAround.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("출구번호\t주변시설")
    for item in itemElements:
        exitno = item.find("exitno")               #출구번호
        dirdesc = item.find("dirdesc")             #주변건물
            
        print(str(exitno.text) + "\t" + str(dirdesc.text))
        
    mail = input("메일? y/n ")
    if mail == 'y':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept, filename)
    elif mail == 'n':
            print("ok....")

#----------------------------------------역 출구별 버스-------------------------------------------
def subwayBus(Code):
    key = "GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D"
    url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnExitAcctoBusRouteList?ServiceKey=" + key + "&subwayStationId=" + Code + "&numOfRows=999&pageSize=999&pageNo=1&startPage=1"
    
    data = urllib.request.urlopen(url).read()

    filename = "subwayBus.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("출구번호\t버스")
    for item in itemElements:
        exitno = item.find("exitno")                     #출구번호
        busrouteno = item.find("busrouteno")             #버스번호
            
        print(str(exitno.text) + "\t" + str(busrouteno.text))
        
    mail = input("메일? y/n ")
    if mail == 'y':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept, filename)
    elif mail == 'n':
        print("ok....")
#---------------------------------------버스 검색---------------------------------------    
def BusSearch(BuscityCode, NodeId):
#http://openapi.tago.go.kr/openapi/service/서비스명(영문)/오퍼레이션명(영문)
#?ServiceKey=서비스키&요청메세지(영문)=숫자또는코드
    
    key = "GL4c4I7sLqwYTOuzI0s9u4Y4IIL4PBJLeyfm%2Bc3lbr0VCuwRSu7TDPP%2FfG45mp%2Bbqia1uiMMhUxzlfnNP2A0bQ%3D%3D"
    url = "http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList?ServiceKey=" + key + "&cityCode=" + BuscityCode + "&nodeId=" + NodeId
    
    data = urllib.request.urlopen(url).read()

    filename = "Bus.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("========버스==========")
    for item in itemElements:
        #if(item.find("infoType")).text == "1":
        arrprevstationcnt = item.find("arrprevstationcnt")  #도착예정버스 남은 정류장 수
        arrtime = item.find("arrtime") #도착예정버스 도착 예상시간 
        nodeid = item.find("nodeid")    #정류소ID
        nodenm = item.find("nodenm")    #정류소명
        routeid = item.find("routeid")  #노선ID
        routeno = item.find("routeno")  #노선번호
        routetp = item.find("routetp")  #노선유형
        
        print(str(arrprevstationcnt.text) + "\t" + str(arrtime.text) + "\t" + str(nodeid.text) + "\t" + str(nodenm.text) + "\t" + str(routeid.text) + "\t" + str(routeno.text) + "\t" +  str(routetp.text) )

        
        mail = input("메일? y/n ")
        if mail == 'y':
            reciept = input("받는 사람 메일 주소: ")
            SendingMail(reciept, filename)
        elif mail == 'n':
            print("ok....")
#-------------------------------------------------------------------------------------------

def SendingMail(reciept, filename):
    import mimetypes
    import mysmtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    
    #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = filename
    
    senderAddr = "1995jihee@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = str(reciept)   # 받는 사람 email 주소.
    
    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Term Project"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), _charset = 'UTF-8' )
    htmlFD.close()
    
    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)
    
    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host,port)
    s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("1995jihee@gmail.com","ghdlghdl11~")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
#--------------------------------------매뉴----------------------------------------------
def printMenu():
    print("\t")
    print("========Menu==========")    
    print("역 키워드검색: k")
    print("지하철 호선별 막차: s")
    print("버스: b")
    print("끝: q")
    print("========Menu==========")
    
#---------------------------------메뉴실행---------------------------------------------------------
def launcherFunction(menu):
    #역 키워드검색
    if menu == 'k':
        StationName = input("키워드 입력: ")
        StationName = StationName.encode('utf-8')
        print(StationName)
        Change(str(StationName))
    #호선별 막차
    elif menu == 's':
        Line = input("호선(1~9호선: 1~9, 인천 1호선: I, 경의중앙선: K, 분당선: B, 공항철도: A, 경춘선: G, 신분당선: S, 수인선: SU): ")
        Day = input("요일(평:1, 토: 2, 일/공: 3): ")
        Inout = input("상(1)/하(2))행선: ")
        if Line == '1':
            End = '100'
        elif Line == '2':
            End = '52'
        elif Line == '3':
            End = '43'
        elif Line == '4':
            End = '47'
        elif Line == '5':
            End = '50'
        elif Line == '6':
            End = '32'
        elif Line == '7':
            End = '50'
        elif Line == '8':
            End = '16'
        elif Line == '9':
            End = '29'
        elif Line == 'I':
            End = '28'
        elif Line == 'K':
            End = '53'
        elif Line == 'B':
            End = '35'
        elif Line == 'A':
            End = '11'
        elif Line == 'G':
            End = '21'
        elif Line == 'S':
            End = '11'
        elif Line == 'SU':
            End = '13'
        subway(End, Line, Day, Inout)
    #지하철역검색
    elif menu == 'g':
        Code = input("검색할 역코드를 입력하세요: ")
        Day = input("요일(평:1, 토: 2, 일/공: 3): ")
        Inout = input("상(1)/하(2))행선: ")
        subwaySearch(Code, Day, Inout)
    elif menu == 'b':
        BuscityCode = input("도시코드: ")
        NodeId = input("정류소: ")
        BusSearch(BuscityCode, NodeId)
    elif menu == 'm':
        reciept = input("받는 사람 메일 주소: ")
        SendingMail(reciept)
    elif menu == 'q':
        print("Thank you! bye~~!")
        global loopFlag
        loopFlag = 0
    else:
        print ("error : unknow menu key")

#-----------------------------------전체 실행---------------------------------------------------------
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)