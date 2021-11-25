import json
import urllib.request

url="https://api.odcloud.kr/api/15094083/v1/uddi:c56fbd05-7fc0-42de-86f6-d9334784049a?page=1&perPage=10&serviceKey="

data = urllib.request.urlopen(url).read()
output = json.loads(data)

print(output)