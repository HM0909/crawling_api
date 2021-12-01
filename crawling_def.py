import json
import urllib.request
import csv

url="https://api.odcloud.kr/api/15094782/v1/uddi:6b2017af-659d-437e-a549-c59788817675?page=2&perPage=20&serviceKey=lY5VDz%2BXyNYWIyMcrdAyz6UeJXh6gcVSr0WpKZFCpFYBr4N7x0LPfnrxX1NZSnFCfcJor1LLLVPFBNEuSvh3pA%3D%3D"

data = urllib.request.urlopen(url).read()
output = json.loads(data)

cf = open("C:/hm_py/crawling/result/crawling_def.csv",'w', newline='')

wr = csv.writer(cf)
wr.writerow(['가격', '경도', '데이터기준일', '명칭', '영업시간', '위도', '재고량', '전화번호', '주소', '코드'])

# json 파일 열기
def open_json():
    jsonArray = output.get("data")

    for list in jsonArray:
        csv_writer(list)

    
# csv 파일 생성
def csv_writer(list):
    wr.writerow([list.get("가격"), list.get("경도"), list.get("데이터기준일"), list.get("명칭"), list.get("영업시간"), list.get("위도"), list.get("재고량"), list.get("전화번호"), list.get("주소"), list.get("코드")])


def main(): 
    
    open_json()
        
    # 파일 닫기
    cf.close()

    
if __name__ == '__main__':
    main()
