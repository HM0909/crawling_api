import json
import urllib.request
import csv

url="http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst?serviceKey=lY5VDz%2BXyNYWIyMcrdAyz6UeJXh6gcVSr0WpKZFCpFYBr4N7x0LPfnrxX1NZSnFCfcJor1LLLVPFBNEuSvh3pA%3D%3D&returnType=json&numOfRows=100&pageNo=1&itemCode=PM10&dataGubun=HOUR&searchCondition=MONTH"

data = urllib.request.urlopen(url).read()
output = json.loads(data)

cf = open("C:/hm_py/crawling/result/crawling_air.csv",'w', newline='')

keys = ["daegu","chungnam","incheon","daejeon","gyeongbuk","sejong","gwangju","jeonbuk","gangwon","ulsan","jeonnam","seoul","busan","jeju","chungbuk","gyeongnam","dataTime","dataGubun","gyeonggi","itemCode"]

wr = csv.writer(cf)
wr.writerow(keys)

# json 파일 열기
def open_json():
    jsonArray = output.get("response")
    body = jsonArray.get("body")
    items = body.get("items")
    
    for item in items:
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