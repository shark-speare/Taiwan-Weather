import requests
import os

# 生成每個天氣小幫手的API網址
apis = [f"https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-0{str(i).zfill(2)}" for i in range(9,31)]
params = {
    'Authorization' : os.environ['WEATHER'],
    'format' : 'JSON'
}

finalList = []
tableList = []

# 分別抓取資訊
for url in apis:
    result = requests.get(url=url,params=params)
    data = result.json()['cwaopendata']['dataset']

    # 地點
    location = data['location']['locationName']
    tableList.append(f"[{location}](#{location})")

    # 合併每一個描述
    lines = data['parameterSet']['parameter']
    description = '\n\n'.join([content['parameterValue'] for content in lines])

    #加入最終列表
    finalList.append(f"# {location}\n{description}")

    print(f"已擷取{location}資料")

final = "\n".join(finalList)
table = "\n".join(tableList)

with open('README.md',mode='w',encoding='utf8') as f:
    f.write(table + "\n" + final)

    