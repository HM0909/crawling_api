import json
import urllib.request
import csv

url="https://api.odcloud.kr/api/15094083/v1/uddi:c56fbd05-7fc0-42de-86f6-d9334784049a?page=1&perPage=10&serviceKey=lY5VDz%2BXyNYWIyMcrdAyz6UeJXh6gcVSr0WpKZFCpFYBr4N7x0LPfnrxX1NZSnFCfcJor1LLLVPFBNEuSvh3pA%3D%3D"

data = urllib.request.urlopen(url).read()
output = json.loads(data)

cf = open("C:/hm_py/crawling/result/crawling_vacc.csv",'w', newline='')

keys= ['10월말(누적) 1차접종자' , '10월말(누적) 2차접종자', '10월말(누적) 추가접종', '2-6월 1차접종자', '2-6월 2차접종자', '7월말(누적) 1차접종자', '7월말(누적) 2차접종자', '8월말(누적) 1차접종자', '8월말(누적) 2차접종자', '9월말(누적) 1차접종자', '9월말(누적) 2차접종자', '자치구']

wr = csv.writer(cf)
wr.writerow(keys)
    
# json 파일 열기
def open_json():
    jsonArray = output.get("data")

    for item in jsonArray:
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