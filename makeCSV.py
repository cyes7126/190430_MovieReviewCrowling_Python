from bs4 import BeautifulSoup
import requests
result_point=[]
result_title=[]
result_report=[]
for i in range(1,10):
    url = "https://movie.naver.com/movie/point/af/list.nhn?page="+str(i)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,'lxml')
    table = soup.find('table',class_="list_netizen")
    tbody = table.find('tbody')
    trArray= tbody.find_all('tr')
    for tr in trArray:
        point = tr.find('td',class_="point").text.strip()
        title = tr.find('td',class_="title").find('a',class_="movie").get_text(strip=True)
        str1 = tr.find('td',class_="title").find('a',class_="report").get('href')
        start = str1.find('(')
        end = str1.find(')')
        str2 = str1[start+1:end]
        arr = str2.split(',')
        report=arr[2]
        print(point)
        print(title)
        print(report)
        result_point.append(point)
        result_title.append(title)
        result_report.append(report)
data = {'point':result_point,'title':result_title,'report':result_report}
print(data)
from pandas import DataFrame
df=DataFrame(data,columns=['point','title','report'])
df.to_csv('movieTest.csv')