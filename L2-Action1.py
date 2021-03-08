# homework-L2-503816-王作伟
import requests
from bs4 import BeautifulSoup
import pandas as pd
# 封装函数
def get_page_content(request_url):
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    # print(content) 打印后发现content内容杂乱，不易分析
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    # 返回值
    return soup
# 分析当前页面的投诉信息
def analysis(soup):
    df = pd.DataFrame(columns = ['id', 'brand', 'car_mould', 'car_type', 'desc', 'prob', 'datetime', 'status'])
    # 找到完整的信息投诉框
    temp = soup.find('div', class_= 'tslb_b')
    # 列出所有的行
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            # 投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态
            id, brand, car_mould, car_type, desc, prob, datetime, status = \
                td_list[0].text, td_list[1].text, \
                td_list[2].text, td_list[3].text, \
                td_list[4].text, td_list[5].text, \
                td_list[6].text, td_list[7].text
            print(id, brand, car_mould, car_type, desc, prob, datetime, status)
            # 数据放到Excel中，通过字典进行排版，更直观
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_mould'] = car_mould
            temp['car_type'] = car_type
            temp['desc'] = desc
            temp['prob'] = prob
            temp['datetime'] = datetime
            temp['status'] = status
            df = df.append(temp, ignore_index=True)
    return df
result = pd.DataFrame(columns = ['id', 'brand', 'car_mould', 'car_type', 'desc', 'prob', 'datetime', 'status'])
# 请求URL，并实现翻页过程
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1'
# 设置抓取页数输入窗口
page_num = int(input('请输入抓取页数：'))
# 通过for循环实现多页连续抓取数据
for i in range(page_num):
    # 拼接每页的数据
    request_url = base_url + str(i+1) + '.shtml'
    # 得到soup的解析
    soup = get_page_content(request_url)
    df = analysis(soup)
    result = result.append(df)
print(result)
result.to_excel('car_complain.xlsx')