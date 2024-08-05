import requests
import os

# 生成每個天氣小幫手的API網址
apis = [f"https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-0{str(i).zfill(2)}" for i in range(9,31)]
params = {
    'Authorization' : 'CWA-3FF8D5E8-035D-4F66-BD63-CFF6EDB21C2D',
    'format' : 'JSON'
}

north = ['台北市','新北市','基隆市','新竹市','桃園市','新竹縣']
middle = ['台中市','苗栗縣','彰化縣','南投縣','雲林縣']
south = ['高雄市','台南市','嘉義市','嘉義縣','屏東縣']
east =  ['花蓮縣','台東縣','宜蘭縣']
out = ['澎湖縣','金門縣','連江縣']

nlist = [f"[{i}](#{i})" for i in north]
mlist =[f"[{i}](#{i})" for i in middle]
slist = [f"[{i}](#{i})" for i in south]
elist = [f"[{i}](#{i})" for i in east]
olist = [f"[{i}](#{i})" for i in out]

finalList = []
table = f'''
北部 | 中部 | 南部 | 東部 | 離島
 --- | --- | --- | --- | ---
{" ".join(nlist)} | {" ".join(mlist)} | {" ".join(slist)} | {" ".join(elist)} | {" ".join(olist)}

'''

# 分別抓取資訊
for url in apis:
    result = requests.get(url=url,params=params)
    data = result.json()['cwaopendata']['dataset']

    # 地點
    location = data['location']['locationName']

    # 合併每一個描述
    lines = data['parameterSet']['parameter']
    description = '\n\n'.join([content['parameterValue'] for content in lines])
    formatted_description = description.replace("~","\~")
    full_description = formatted_description.replace('（','(')
    full_description_2 = formatted_description.replace("）")')
                                                           

    #加入最終列表
    finalList.append(f"# {location}\n{full_description_2}")

    print(f"已擷取{location}資料")

final = "\n".join(finalList)

with open('README.md',mode='w',encoding='utf8') as f:
    f.write(table + "\n" + final)

    
