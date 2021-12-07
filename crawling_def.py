import json
import urllib.request
import csv

url="https://api.odcloud.kr/api/15094782/v1/uddi:6b2017af-659d-437e-a549-c59788817675?page=2&perPage=20&serviceKey=lY5VDz%2BXyNYWIyMcrdAyz6UeJXh6gcVSr0WpKZFCpFYBr4N7x0LPfnrxX1NZSnFCfcJor1LLLVPFBNEuSvh3pA%3D%3D"

data = urllib.request.urlopen(url).read()
output = json.loads(data)

cf = open("C:/hm_py/crawling/result/crawling_def.csv",'w', newline='')

keys = ['가격', '경도', '데이터기준일', '명칭', '영업시간', '위도', '재고량', '전화번호', '주소', '코드']

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
