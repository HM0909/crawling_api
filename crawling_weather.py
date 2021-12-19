import json
import urllib.request
import csv

url="http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnWthrIdx?serviceKey=lY5VDz%2BXyNYWIyMcrdAyz6UeJXh6gcVSr0WpKZFCpFYBr4N7x0LPfnrxX1NZSnFCfcJor1LLLVPFBNEuSvh3pA%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2019122010&HOUR=24&COURSE_ID=1"

data = urllib.request.urlopen(url).read()
output = json.loads(data)

cf = open("C:/hm_py/crawling/result/crawling_weather.csv",'w', newline='')

keys = ["tm", "thema", "courseId", "courseAreaId", "courseAreaName", "courseName", "spotAreaId", "spotAreaName", "spotName", "btIndex", "fdIndex", "uvIndex", "htIndex", "dsIndex", "piIndexCharm", "piIndexSo", "piIndexWeed"] 

wr = csv.writer(cf)
wr.writerow(keys)

# json 파일 열기
def open_json():
    jsonArray = output.get("response")
    body = jsonArray.get("body")
    items = body.get("items")
    item_list = items.get("item")
    
    for item in item_list:
        list = []
        
        for i in range(len(keys)):
            list.append(item.get(keys[i]))
            
        csv_writer(list)

    
# csv 파일 생성
def csv_writer(list):
    wr.writerow(list)
    

def main(): 
    
    open_json()
        
    # 파일 닫기
    cf.close()

    
if __name__ == '__main__':
    main()