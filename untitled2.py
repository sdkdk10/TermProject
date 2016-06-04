import urllib.request
import xml.etree.ElementTree as etree

loopFlag = 1

#-------------------------------도시코드-----------------------------------------------
def cityCode():

    key = 'GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D'
    url = "http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList?ServiceKey=" + key

    data = urllib.request.urlopen(url).read()

    filename = "citycode.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()
    
    #파싱하기
    tree = etree.parse(filename)    
    itemElements = tree.getiterator("item")
    print("items")
    for item in itemElements:
        #if(item.find("infoType")).text == "1":
        code = item.find("code")
        sname = item.find("sname")

        print(str(code.text) + "\t" + str(sname.text))


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
        #if(item.find("infoType")).text == "1":
#        LINE_NUM = item.find("LINE_NUM")                 #호선
#        WEEK_TAG = item.find("WEEK_TAG")                 #요일
#        INOUT_TAG = item.find("INOUT_TAG")               #상/하행선
        FR_CODE = item.find("FR_CODE")                   #외부코드
        STATION_CD = item.find("STATION_CD")             #전철역코드
        STATION_NM = item.find("STATION_NM")             #전철역명
        FIRST_TIME = item.find("FIRST_TIME")             #첫차시간
#        F_ORIGINSTATION = item.find("F_ORIGINSTATION")   #첫차출발역코드
        F_SUBWAYSNAME = item.find("F_SUBWAYSNAME")       #첫차출발역명
        LAST_TIME = item.find("LAST_TIME")               #막차시간
#        L_ORIGINSTATION = item.find("L_ORIGINSTATION")   #막차출발역코드
        L_SUBWAYSNAME = item.find("L_SUBWAYSNAME")       #막차출발역명
#        L_DESTSTATION = item.find("L_DESTSTATION")       #막차도착역코드
        L_SUBWAYENAME = item.find("L_SUBWAYENAME")       #막차도착역명
            
        print(str(FR_CODE.text) + "\t" + str(STATION_CD.text)+  "\t" + str(STATION_NM.text)
        + "\t" + str(FIRST_TIME.text) + "\t" + str(F_SUBWAYSNAME.text) + "\t" + str(LAST_TIME.text)  
        + "\t" + str(L_SUBWAYSNAME.text) + "\t" + str(L_SUBWAYENAME.text))
    
#---------------------------------지하철역검색----------------------------------------------------------------
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
    
#--------------------------------------매뉴----------------------------------------------
def printMenu():
    print("막차시간정보")
    print("========Menu==========")    
    print("도시코드:  l")
    print("지하철 호선별 막차: s")
    print("지하철역막차검색: g")
    print("========Menu==========")
    
#---------------------------------메뉴실행---------------------------------------------------------
def launcherFunction(menu):
    #도시코드
    if menu ==  'l':
        cityCode()
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
    else:
        print ("error : unknow menu key")

#-----------------------------------전체 실행---------------------------------------------------------
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)